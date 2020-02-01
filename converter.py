import json
import yaml

def generate_yaml_doc(yaml_file,yaml_obj):
    file = open(yaml_file, 'w', encoding='utf-8')
    yaml.dump(yaml_obj, file)
    file.close()

with open("general.json",'r',encoding='utf-8') as f:
    jsonData = json.loads(f.read(),encoding = "UTF-8")
    f.close()
warps = jsonData['warps']
worldDict = {"a5fc0708-a108-4ad0-9a8a-343f969895f4":"world","b67354ef-9cb9-400e-9b0a-f34f1d889306":"world_nether","d41f9cb5-3237-4e32-82dc-fbd6bc2b6cea":"world_the_end"}
owner = "f701cc46-e710-33fd-8d35-73364be91f27"
counter = 0
for name in warps:
    worldname = worldDict[warps[name]["world"]]
    warpobj = {'world':worldname,'x':warps[name]['x'],'y':warps[name]['y'],'z':warps[name]['z'],'yaw':warps[name]['roty'],'pitch':warps[name]['rotx'],'name':name,'lastowner':owner}
    generate_yaml_doc(name.lower()+".yml",warpobj)
    print("Converted: "+worldname+":"+name);
    counter+=1
print("="*12)
print(counter,"warps converted.")

