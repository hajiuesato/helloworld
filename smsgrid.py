#!/bin/env python 
# smsgrid.py
# git commit!!!
# adding a feature

import sys,os,re,csv

icon_size       = "150x84" #"295x166"
picon_w         = "90"
picon_h         = "50"
CSV             = "/u/haji/scripts/smsgrid/sms.6.csv"
student_albums  = "/u/haji/scripts/smsgrid/student_albums.csv"
log             = "/u/haji/scripts/smsgrid/log.txt"
www             = "/u/haji/scripts/smsgrid/index.html"
aaa = {'album': '2877313', '': '', 'datecode': '140517', 'description': 'End of Year', 'grade': '7', 'video': '95574888', 'student': 'vian', 'icon': '475537146'}


class DB:
  def __init__ (self):
    self.objects = {}
    
  def add_object(self,row):
    self.objects.update(row)

  def get_datecodes(self):
    all_datecodes = [];
    
    for o in data.objects:
      all_datecodes.append(data.objects[o]['datecode']);
    
    all_datecodes = set(all_datecodes);
    all_datecodes = list(all_datecodes);
    all_datecodes.sort();
    
    return all_datecodes
    

  def info(self,datecode,student):    
    datecode_hits = {}
    student_hits  = {}
    s ={}
    info_dict     = {'description':'','last_name':'','first_name':'','video_url':'','icon_url':'','album_url':''};
    
    ### search for datecode in all objects and put results into datecode_hits
    for o in data.objects:
      if (data.objects[o]["datecode"] == datecode):
        key = data.objects[o]["student"];
        datecode_hits.update({key:data.objects[o]});

    ### use first key in datecode_hits to assign all shared performance variables
    first_key = datecode_hits.keys()[0]; 

    if (datecode_hits[first_key]["grade"]   == "K"):
      grade = "Kindergarten"
    elif (datecode_hits[first_key]["grade"] == "1"):
      grade = "1st Grade";
    elif (datecode_hits[first_key]["grade"] == "2"):
      grade = "2nd Grade";
    elif (datecode_hits[first_key]["grade"] == "3"):
      grade = "3rd Grade";
    else:
      grade = str(datecode_hits[first_key]["grade"]) + "th Grade";

    info_dict["description"] = grade + " " + str(datecode_hits[first_key]["description"]) + " Concert";
    info_dict["album_url"]   = "https://vimeo.com/album/" + str(datecode_hits[first_key]["album"]);
    info_dict["last_name"]   = full_name(student)[1];
    info_dict["first_name"]  = full_name(student)[0];
    
    ### test whether student played in the concert   
    if datecode_hits.get(student): 
      s = datecode_hits.get(student);  
      info_dict['video_url'] = "https://vimeo.com/" + str(s['video']);
      info_dict['icon_url']  = "https://i.vimeocdn.com/video/" + str(s['icon']) + "_" + str(icon_size) + ".jpg"
    else:
      info_dict['video_url'] = "-";
      info_dict['icon_url']  = "-"
#       info_dict['video_url'] = "file:///u/haji/scripts/smsgrid/black.jpg";
#       info_dict['icon_url']  = "file:///u/haji/scripts/smsgrid/black.jpg";
      
    return info_dict;


def full_name(name):
  global full_name_dict;
  full_name_dict = {    
    'abe':('Abe','Gold'),
    'alice':('Alice','Volfson'),
    'annaliese':('Annaliese','Wee'),
    'anthony':('Anthony','Choi'),
    'bryan':('Bryan','Bedford'),
    'daniel':('Daniel','Ma'),
    'giorgio':('Giorgio','Poma'),
    'gregory':('Gregory','Llewellyn'),
    'hannah':('Hannah','Rudt'),
    'harry':('Harry','Wang'),
    'hazel':('Hazel','Carrasco'),
    'howard':('Howard','Lin'),
    'isabelj':('Isabel','Janovsky'),
    'isabelk':('Isabel','Kingston'),
    'janine':('Janine','Goh'),
    'loris':('Loris','Jaoutakas'),
    'luca':('Luca','Sakon'),
    'max':('Max','Simeone'),
    'misha':('Misha','Ellis'),
    'myah':('Myah','Segura'),
    'nika':('Nika','Gurwitz'),
    'nils':('Nils','Krarup'),
    'nina':('Nina','Uesato'),
    'shai':('Shai','Rodriguez'),
    'sophia':('Sophia','Manuguerra'),
    'taja':('Taja','Graves-Parker'),
    'vian':('Vian','Wagatsuma'),
  }

  first_name = full_name_dict[name][0];
  last_name  = full_name_dict[name][1];

  return first_name,last_name;


def print_info(datecode,student):
  a = data.info(datecode,student);
  print str(a["first_name"]) + " " + str(a["last_name"]);
  print a["description"];
  print a["album_url"];
  print a["video_url"];
  print a["icon_url"];
  print "";
  
def print_and_log_info(datecode,student):
  a  = data.info(datecode,student);
  aa = str(a["first_name"]) + " " + str(a["last_name"]) + "\n" + str(a["description"]) + "\n" + str(a["album_url"]) + "\n" + str(a["video_url"]) + "\n" + str(a["icon_url"]) + "\n"
  return aa
  
def html_addcell(datecode,student):
  a  = data.info(datecode,student);

  if (a["video_url"] != "-"):
    rollover_text = str(student) + " - " + str(a["description"]);
    aa = "    <td class=\"tg-s6z2\"><a href=\"" + str(a["video_url"]) + "\" target=\"_blank\"><img src=\"" + str(a["icon_url"]) + "\"width=\"" + str(picon_w) + "\" height=\"" + str(picon_h) + "\" alt=\"" + str(rollover_text) + "\" title=\"" +  str(rollover_text) + "\"'></a></td>\n";
  else:
    aa = "    <td></td>\n";
  return aa
 
  
def student_album_url(student):
  global student_album_dict;
  student_album_dict = {    
    'abe':'3320203',
    'alice':'3318951',
    'annaliese':'3318925',
    'anthony':'3320222',
    'bryan':'3318903',
    'daniel':'3320179',
    'giorgio':'3320455',
    'gregory':'3320166',
    'hannah':'3318875',
    'harry':'3318873',
    'hazel':'3320009',
    'howard':'3318884',
    'isabelj':'3318712',
    'isabelk':'3318863',
    'janine':'3318856',
    'loris':'3318840',
    'luca':'3319988',
    'max':'3318828',
    'misha':'3318833',
    'myah':'3318803',
    'nika':'3318971',
    'nils':'3318953',
    'nina':'3318788',
    'shai':'3318723',
    'sophia':'3318726',
    'taja':'3318721',
    'vian':'3318719',
  }

  url = student_album_dict[student];
  return url;

  



def main():
  global data;
  data = DB();
  all_students  = [];
  all_concerts  = [];
  ### html_concerts = ['061215', '070518', '071214', '080523', '090522', '091211', '100326', '100604', '101210', '110325', '110527', '111216', '120323', '120518', '121214', '130525', '131213', '140310', '140517', '141205'];  # includes spring and bucket
  html_concerts = ['061215', '070518', '071214', '080523', '081212', '090522', '091211', '100326', '100604', '101210', '110325', '110527', '111216', '120323', '120518', '121214', '130525', '131213', '140310', '140517', '141205', '150320', '150515'];  

  ### load csv data into database
  i = 1;
  with open(CSV) as f:
      f_csv = csv.DictReader(f)
      for row in f_csv:
        object_id = "object_" + str(i);
        data.add_object({object_id:row});      
        i += 1;


#   ### get names of all students
#   full_name('nina');
#   for key in full_name_dict:
#     all_students.append(key);
#     all_students.sort();
      
  ### hardcode all students in last name order
  all_students = ['bryan','hazel','anthony','misha','janine','abe','taja','nika','isabelj','loris','isabelk','nils','howard','gregory','daniel','sophia','giorgio','shai','hannah','luca','myah','max','nina','alice','vian','harry','annaliese']

  ### get datecodes of all concerts
  all_concerts = data.get_datecodes();
    




  print all_students;
  print all_concerts;
  
  ### show all of each student's concerts
  l = open(log,'w')  
  for student in all_students:
    for concert in all_concerts:
      info = print_and_log_info(concert,student)
      print(info)
      l.write(info)
      l.write('\n')
  l.close()

  ### make html of each student's sms concerts
  # write header
  h = open(www,'w')
  h.write('\
<style type=\"text/css\">\n\
  a {text-decoration: none}\n\
  a {color : #444}\n\
  .tg  {border-collapse:collapse;border-spacing:0;}\n\
  .tg td{font-family:Arial, sans-serif;font-size:12px;padding:7px 2px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#000000;color:#333;background-color:#000000;}\n\
  .tg th{font-family:Arial, sans-serif;font-size:12px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#000000;color:#FFF;font-weight:bold;background-color:#000000;}\n\
  .tg .tg-s6z2{text-align:center}\n\
  .tg .tg-0ord{text-align:right}\n\
</style>\n\n')

  h.write('\
<body bgcolor="#000000">\n\
<table class=\"tg\">\n\
  <tr>\n\
    <th class=\"tg-031e\"></th>\n\
    <th class=\"tg-031e\"></th>\n\
    <th class=\"tg-s6z2\" colspan=\"2\">Kindergarten</th>\n\
    <th class=\"tg-s6z2\" colspan=\"2\">1st Grade<br></th>\n\
    <th class=\"tg-s6z2\" colspan=\"2\">2nd Grade<br></th>\n\
    <th class=\"tg-s6z2\" colspan=\"3\">3rd Grade<br></th>\n\
    <th class=\"tg-s6z2\" colspan=\"3\">4th Grade<br></th>\n\
    <th class=\"tg-s6z2\" colspan=\"3\">5th Grade<br></th>\n\
    <th class=\"tg-s6z2\" colspan=\"2\">6th Grade<br></th>\n\
    <th class=\"tg-s6z2\" colspan=\"3\">7th Grade<br></th>\n\
    <th class=\"tg-s6z2\" colspan=\"3\">8th Grade<br></th>\n\
  </tr>\n\n\
  <tr>\n\
    <td class=\"tg-031e\"></td>\n\
    <td class=\"tg-031e\"></td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/3169080\" target=\"_blank\">Mid-Year</a></td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/3175943\" target=\"_blank\">End of Year</a></td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/2667135\" target=\"_blank\">Mid-Year</a></td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/2667933\" target=\"_blank\">End of Year</a></td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/3194444\" target=\"_blank\">Mid-Year</a></td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/1495037\" target=\"_blank\">End of Year</td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/2665156\" target=\"_blank\">Mid-Year</a></td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/1491331\" target=\"_blank\">Spring Grade</a></td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/1491336\" target=\"_blank\">End of Year</td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/1491345\" target=\"_blank\">Mid-Year</a></td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/1560920\" target=\"_blank\">Spring Grade</a></td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/1609268\" target=\"_blank\">End of Year</td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/1780498\" target=\"_blank\">Mid-Year</a></td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/1881834\" target=\"_blank\">Spring Grade</td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/1943825\" target=\"_blank\">End of Year</td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/2188413\" target=\"_blank\">Mid-Year</a></td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/2399458\" target=\"_blank\">End of Year</td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/2649407\" target=\"_blank\">Mid-Year</a></td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/2771167\" target=\"_blank\">Bucket</a></td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/2877313\" target=\"_blank\">End of Year</td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/3162807\" target=\"_blank\">Mid-Year</a></td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/3314380\" target=\"_blank\">Exit Project</a></td>\n\
    <td class=\"tg-s6z2\"><a href=\"https://vimeo.com/album/3397464\" target=\"_blank\">End of Year</a></td>\n\
  </tr>\n\n')

  # write student rows
  for student in all_students:
    h.write('  <tr>\n')
#     h.write('    <td class=\"tg-0ord\">' + str(full_name(student)[0]) + '</td>\n')
#     h.write('    <td class=\"tg-031e\">' + str(full_name(student)[1]) + '</td>\n')
    h.write('    <td class=\"tg-0ord\"><a href=\"https://vimeo.com/album/' + str(student_album_url(student)) + '" target=\"_blank\">' + str(full_name(student)[0]) + '</td>\n')
    h.write('    <td class=\"tg-031e\"><a href=\"https://vimeo.com/album/' + str(student_album_url(student)) + '" target=\"_blank\">' + str(full_name(student)[1]) + '</td>\n')
    for concert in html_concerts:
      html = html_addcell(concert,student)
#       print(html)
      h.write(html)
    h.write('  </tr>\n\n')
  h.write('</table>\n\
  </body>\n')
  h.close()

#   print all_students;
#   print all_concerts;
#   print html_concerts;


if __name__ == '__main__':
  main()
