# Step 1: Download all transcripts (slides and videos, quizzes) using this tutorial: https://www.youtube.com/watch?v=xRk7TPobFvg&t=4s
# Step 2: Move all chapter folders (or the entire course) to the same directory
# step 3: Run the scipt below

import os
path = r'E:\Coursera\courseX'
line_size = 74
count = 0
txt_list = []
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.en.txt'):
            count += 1
            txt = ['    ']
            with open(os.path.join(root, file), 'r') as document:
                for line in document:
                    line = line.replace('[MUSIC]', '').replace('[SOUND]', '').replace('[COUGH]', '').replace('[LAUGH]', '').replace('>> ', '')
                    txt.append(line)
            txt = [x.replace('\n', '') for x in txt]
            txt = " ".join(txt)
            i = 0
            txt_list.append('WEEK ' + root.split('\\')[-2].replace('_', ' ').replace('-', ' ')[8:].upper() + '\n')
            title = root.split('\\')[-1].replace('_', ' ').replace('-', ' ')[3:].upper() + ': ' + file.replace('_', ' ').replace('-', ' ').replace('.en.txt', '')[3:] + '\n\n'
            title = title.replace('WEEK 9 ', '').replace('WEEK 15 ', '')
            txt_list.append(title)
            while len(txt)>line_size:
                i +=1
                if i>line_size:
                    if len(txt)> i:
                        if txt[i]==" ":
                            txt_list.append(txt[:i]+' ')
                            txt = txt[i+1:]
                            i = 0
                    else: 
                        txt_list.append(txt + ' ')
                        txt = ""
                        i=0
            txt_list.append('\n\n\n')
    
with open(os.path.join(path, 'summary.txt'), 'w') as output:
    for text in txt_list:
        output.write(text)
print(f'Transcripts of all {count} videos were created')
