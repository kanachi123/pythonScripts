import bpy #blender api
import os #os file system moduls 
import urllib.request #libcurl аналог
#получаем ссылку на репозитории
github_zip_url = "https://github.com/danielenger/Principled-Baker/archive/refs/heads/master.zip"#аддон для pbr текстур
#временная папка
temp_dir = bpy.app.tempdir
#дестинейшн для установки
zip_path =os.path.join(temp_dir,"Principled-Baker.zip")
#запрос на скачивание как curl
urllib.request.urlretrieve(github_zip_url,zip_path)
#сразу устанавливаем в блендер
bpy.ops.preferences.addon_install(filepath=zip_path,overwrite=True)
#для активации имя модуля меняем - на _,чтобы соответсвовало __init__
module_name = "Principled-Baker".replace("-","_")

try:#если имя аддона написали правильно активируем
    bpy.ops.preferences.addon_enable(module=module_name)
    print("enabled")
except Exception as e:
    print("enable error")
bpy.ops.wm.save_userpref()#save config
print("addon is enabled")
