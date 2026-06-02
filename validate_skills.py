import re, yaml, glob

skills = glob.glob('/home/ubuntu/hermes-rocha-family/skills/home-assistant/**/SKILL.md', recursive=True)
for path in skills:
    content = open(path).read()
    assert content.startswith('---'), f'{path}: must start with ---'
    m = re.search(r'\n---\s*\n', content[3:])
    assert m, f'{path}: frontmatter must close'
    fm = yaml.safe_load(content[3:m.start()+3])
    assert 'name' in fm and 'description' in fm
    assert fm['description'].startswith('Use when'), f'{path}: description must start with Use when'
    assert len(fm['description']) <= 1024
    print(f"OK {fm['name']}")

print(f"\nTotal: {len(skills)} skills validated")
