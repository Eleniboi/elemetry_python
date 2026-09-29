import copy

def add_tag(profile, tag):

    updated = profile.copy()

    updated["tags"] = list(profile['tags']) #copy.deepcopy(profile['tags'])

    updated["tags"].append(tag)
    return updated

original = {"name": "Ada", "tags": ["python"]}

changed = add_tag(original, "testing")

print(original["tags"])
print(changed["tags"])
print(changed is original)
print(changed["tags"] is original["tags"])