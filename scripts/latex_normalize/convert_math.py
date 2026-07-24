#!/usr/bin/env python3
"""Convert Unicode/plaintext statistics notation to LaTeX ($...$) in MyST .md.

Token-based so English words break math runs (no wrapping whole sentences).
Protects existing math / inline code / fenced code verbatim.
"""
import re, sys

GREEK = {
    'α':r'\alpha','β':r'\beta','γ':r'\gamma','δ':r'\delta','ε':r'\varepsilon',
    'μ':r'\mu','σ':r'\sigma','ρ':r'\rho','λ':r'\lambda','π':r'\pi','θ':r'\theta',
    'τ':r'\tau','χ':r'\chi','φ':r'\phi','ω':r'\omega','ν':r'\nu','η':r'\eta',
    'Σ':r'\Sigma','Δ':r'\Delta','Π':r'\Pi','Ω':r'\Omega','Φ':r'\Phi',
}
REL = {
    '≈':r'\approx','≠':r'\neq','≤':r'\leq','≥':r'\geq','±':r'\pm',
    '×':r'\times','÷':r'\div','·':r'\cdot','∼':r'\sim','∝':r'\propto',
    '→':r'\to','∞':r'\infty','∈':r'\in','∉':r'\notin','∪':r'\cup','∩':r'\cap',
    '∅':r'\emptyset','≡':r'\equiv','∓':r'\mp',
}
SUB = {'₀':'0','₁':'1','₂':'2','₃':'3','₄':'4','₅':'5','₆':'6','₇':'7','₈':'8','₉':'9',
       'ₐ':'a','ₑ':'e','ₒ':'o','ₓ':'x','ᵢ':'i','ⱼ':'j','ₙ':'n','ₖ':'k','ₚ':'p','ₜ':'t'}
SUP = {'²':'2','³':'3','⁴':'4','¹':'1','⁰':'0','⁵':'5','ⁿ':'n'}
FRAC = {'½':r'\tfrac12','¼':r'\tfrac14','¾':r'\tfrac34','⅓':r'\tfrac13','⅔':r'\tfrac23'}
MINUS='−'; MACRON='̄'; CIRCUM='̂'
STRONG = set(GREEK)|set(REL)|set(SUB)|set(SUP)|set(FRAC)|{'√',MACRON,CIRCUM}
STRONG_RE = re.compile('['+re.escape(''.join(STRONG))+']')

CODE_DIRECTIVES={'code-cell','code','raw','literalinclude','math','mermaid'}
def _is_code_fence(info):
    info=info.strip()
    if info.startswith('{'):
        name=info[1:].split('}')[0].strip()
        return name in CODE_DIRECTIVES
    return True  # bare ``` or a language like python/r/text -> code

def protect(text):
    stash=[]
    def keep(s):
        stash.append(s); return f'\x00{len(stash)-1}\x00'
    # Block-protect only true code fences (and already-LaTeX {math}/{raw} etc.),
    # leaving prose directives like {admonition}/{note} open for conversion.
    lines=text.split('\n'); out=[]; i=0
    fence=re.compile(r'^(\s*)(`{3,}|~{3,})(.*)$')
    while i<len(lines):
        m=fence.match(lines[i])
        if m:
            marker=m.group(2); info=m.group(3)
            j=i+1
            while j<len(lines):
                mc=fence.match(lines[j])
                if mc and mc.group(2)[0]==marker[0] and mc.group(3).strip()=='':
                    break
                j+=1
            block='\n'.join(lines[i:j+1]) if j<len(lines) else '\n'.join(lines[i:])
            if _is_code_fence(info):
                out.append(keep(block))
            else:
                out.append(block)   # leave prose-directive block for conversion
            i=j+1
        else:
            out.append(lines[i]); i+=1
    text='\n'.join(out)
    text=re.sub(r'\$\$.*?\$\$', lambda m:keep(m.group(0)), text, flags=re.S)
    text=re.sub(r'(?<!\$)\$(?!\$)[^\n$]*?\$', lambda m:keep(m.group(0)), text)
    text=re.sub(r'`[^`\n]*`', lambda m:keep(m.group(0)), text)
    return text, stash

def restore(text, stash):
    return re.sub(r'\x00(\d+)\x00', lambda m: stash[int(m.group(1))], text)

def to_latex(run):
    out=[]; i=0; n=len(run)
    while i<n:
        c=run[i]
        if c in (MACRON,CIRCUM):
            cmd=r'\bar' if c==MACRON else r'\hat'
            if out and re.fullmatch(r'[A-Za-z]', out[-1]): out[-1]=cmd+'{'+out[-1]+'}'
            i+=1; continue
        if c in GREEK: out.append(GREEK[c]); i+=1; continue
        if c in REL:   out.append('\x01'+REL[c]+'\x01'); i+=1; continue
        if c in FRAC:  out.append(FRAC[c]); i+=1; continue
        if c=='√':
            j=i+1
            if j<n and run[j]=='(':
                depth=0;k=j
                while k<n:
                    if run[k]=='(':depth+=1
                    elif run[k]==')':
                        depth-=1
                        if depth==0:k+=1;break
                    k+=1
                out.append(r'\sqrt{'+to_latex(run[j+1:k-1])+'}'); i=k; continue
            m=re.match(r'[0-9A-Za-z.]+', run[j:]); arg=m.group(0) if m else ''
            out.append(r'\sqrt{'+arg+'}'); i=j+len(arg); continue
        if c in SUB:
            j=i;s=''
            while j<n and run[j] in SUB: s+=SUB[run[j]]; j+=1
            out.append('_{'+s+'}' if len(s)>1 else '_'+s); i=j; continue
        if c in SUP:
            j=i;s=''
            while j<n and run[j] in SUP: s+=SUP[run[j]]; j+=1
            out.append('^{'+s+'}' if len(s)>1 else '^'+s); i=j; continue
        if c==MINUS: out.append('-'); i+=1; continue
        out.append(c); i+=1
    s=''.join(out)
    s=re.sub(r'(\d),(\d{3})(?!\d)', r'\1{,}\2', s)
    s=s.replace('\x01',' ')
    s=re.sub(r'\s+',' ',s).strip()
    return s

OP_RE   = re.compile(r'^[=<>+/±×÷·∼−\-]+$')
NUM_RE  = re.compile(r'^[-−]?\d[\d.,]*%?$')
VAR_RE  = re.compile(r'^[A-Za-z]$')
DIST_RE = re.compile(r'^[a-zA-Z]\(\d+(,\d+)?\)$')   # t(124), F(2,97)

def peel(tok):
    """Return (lead, core, trail): strip leading/trailing prose punctuation,
    keeping decimals and balanced parens intact."""
    lead=''; trail=''
    while tok and tok[0] in '"“‘[*':
        lead+=tok[0]; tok=tok[1:]
    while tok:
        ch=tok[-1]
        if ch in '.,;:!?"”’]':
            trail=ch+trail; tok=tok[:-1]; continue
        break
    return lead, tok, trail

def is_math_tok(core):
    if not core: return None
    if STRONG_RE.search(core): return 'STRONG'
    if OP_RE.match(core):      return 'OP'
    if DIST_RE.match(core):    return 'DIST'
    if NUM_RE.match(core):     return 'NUM'
    if VAR_RE.match(core):     return 'VAR'
    if re.fullmatch(r'[0-9.,()/*+^_=<>±×÷−\-]+', core) and any(c.isdigit() for c in core):
        return 'EXPR'
    return None

def wrap_line(line):
    parts=re.split(r'(\s+)', line)   # words and whitespace, alternating
    toks=[]
    for idx,p in enumerate(parts):
        if p and not p.isspace():
            lead,core,trail=peel(p)
            toks.append([idx,p,lead,core,trail,is_math_tok(core)])
    def gap_ok(a,b):
        return (b[0]==a[0]+2 and parts[a[0]+1]==' '
                and a[4]=='' and b[2]=='')
    runs=[]; i=0
    while i<len(toks):
        if toks[i][5] is None: i+=1; continue
        j=i
        while j+1<len(toks) and toks[j+1][5] is not None and gap_ok(toks[j],toks[j+1]):
            j+=1
        runs.append((i,j)); i=j+1
    for (a,b) in runs:
        while a<=b and toks[a][5]=='OP': a+=1
        while b>=a and toks[b][5]=='OP': b-=1
        if a>b: continue
        types={toks[k][5] for k in range(a,b+1)}
        has_signal = ('STRONG' in types) or ('DIST' in types)
        has_eq = ('OP' in types) and (('NUM' in types) or ('VAR' in types) or ('EXPR' in types)) and (b>a)
        if not (has_signal or has_eq):
            continue
        if a==b and toks[a][5] in ('NUM','VAR','EXPR'):
            continue
        first=toks[a]; last=toks[b]
        joined=' '.join(toks[k][3] for k in range(a,b+1))
        latex=to_latex(joined)
        parts[first[0]]=f'{first[2]}${latex}${last[4]}'
        for pi in range(first[0]+1,last[0]+1):
            parts[pi]=''
    return ''.join(parts)

def convert(text):
    text, stash = protect(text)
    text='\n'.join(wrap_line(ln) for ln in text.split('\n'))
    text=text.replace('−','-')   # stray typographic minus -> hyphen
    return restore(text, stash)

if __name__=='__main__':
    data=sys.stdin.read() if len(sys.argv)<2 else open(sys.argv[1],encoding='utf-8').read()
    sys.stdout.write(convert(data))
