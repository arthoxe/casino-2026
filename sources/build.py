import re, sys, os
D=os.path.dirname(os.path.abspath(__file__))
base=open(os.path.join(D,'base.html')).read()
kit=open(os.path.join(D,'kit.js')).read()
WRAP_A='<!doctype html>\n<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}img{max-width:100%}</style></head><body>\n'
WRAP_B='\n</body></html>\n'
def build(name):
    src=open(os.path.join(D,name+'.game')).read()
    parts=dict(re.findall(r'^@@(\w+)\n(.*?)(?=^@@\w+\n|\Z)',src,re.S|re.M))
    meta=dict(l.split('=',1) for l in parts['META'].strip().splitlines())
    out=base
    if meta.get('lib'):
        out=out.replace('<script>\n(()=>{','<script src="'+meta['lib']+'"></script>\n<script>\n(()=>{',1)
    rep={'TITLE':meta['title'],'ICON':meta['icon'],'NAME_A':meta['a'],'NAME_B':meta['b'],'KEY':meta['key'],'KEYHINT':meta['keyhint'],
         'CSS':parts.get('CSS',''),'PARAMS':parts.get('PARAMS',''),'AUTOPARAMS':parts.get('AUTO',''),'STAGE':parts.get('STAGE',''),'KIT':kit,'GAME':parts['JS']}
    for k,v in rep.items():
        out=out.replace('{{'+k+'}}',v)
    assert '{{' not in out.replace('{{G','') , re.findall(r'\{\{\w+\}\}',out)
    open(os.path.join(D,'..',name+'.html'),'w').write(out)
    os.makedirs(os.path.join(D,'..','casino'),exist_ok=True)
    open(os.path.join(D,'..','casino',name+'.html'),'w').write(WRAP_A+out+WRAP_B)
    js=re.search(r'<script>(.*)</script>',out,re.S).group(1)
    open(os.path.join(D,name+'.check.js'),'w').write(js)
    print('built',name,len(out))
for n in sys.argv[1:]: build(n)
