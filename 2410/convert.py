import os

directory = 'nussoc.github.io/2410/games/round_1'

sub_to_name = {2300089: 'Alvina Png',
 2302373: 'Brian Yeo Zheng Yu',
 2308957: 'Chan Jun Jie',
 2300578: 'Cheng Zhenyu',
 2301842: 'Cheok An Yee',
 2297759: 'Cheong Shao Hong, Justin',
 2295919: 'Chew Wei Jie',
 2300787: 'Choo Kai Xi Kasey',
 2299921: 'Chua Chloe',
 2294680: 'Chung Chee Yong, Darren',
 2301362: 'Damien Foo Xu Xian',
 2310057: 'Darin Chow',
 2301742: 'Dennis Xu Zicong',
 2303502: 'Do Minh Nguyet',
 2298777: 'Ear Hong Wee',
 2304396: 'Ethan Gan Jian Feng',
 2300332: 'Hao Yushun',
 2303310: 'Haren Raj',
 2310222: 'Heng Jia Rong Bryan',
 2291372: 'Hoang Anh Minh',
 2301864: "Jaine Lin Jing'En",
 2299528: 'Jeffrey Liu Weixuan',
 2305117: 'Jose Loh He Xi',
 2300562: 'Kaylen Yeo',
 2303330: 'Kenneth Christopher Hendra',
 2286862: 'Kevin Quah Wei-En',
 2299893: 'Ko Siu Chun',
 2301431: 'Koh Zhi Heng, Timothy',
 2301069: 'Le Viet Anh',
 2300091: 'Lee Yong Rui',
 2302809: 'Li Zhuo Rui, Max',
 2295214: 'Lim Pei En Nichelle',
 2301368: 'Lim Wei Lun, Marcus',
 2302427: 'Lin Xinyan',
 2304103: 'Loh Ruo Yi',
 2299681: 'Loo Yu Xiang',
 2299264: 'Lua Jun Boon',
 2304385: 'Oh Jun En',
 2305744: 'Ong Zhao En',
 2303303: 'Quek Jun Yang',
 2304571: 'Ranga Sahasra',
 2303365: 'Revata Gotama Gandalf',
 2298193: 'Ryan Low Zhe Hao',
 2297028: 'Steven Nathanael Mulyadi',
 2305239: 'Tan Yi Long',
 2305446: 'Teh Jing Da',
 2305241: 'Teoh Chee Hong',
 2295743: 'Ter Xiao Wei',
 2310280: 'Thiam Jia Qi, Valencia',
 2299982: 'Toh Xian Zong',
 2300377: 'Wong Yao Feng, Gareth',
 2309312: 'Xu Duanyang',
 2301830: 'Yao William',
 2295929: 'Yap Han Keat',
 2299699: 'Ye Fan',
 2301668: 'Yeo Xin Hui Valerie',
 2299956: 'Yu Hao Jen',
 2300204: 'Zhuo Huangyi',
 2303379: 'Zou Gongwang'}

# Process each HTML file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        
        # Read the HTML file
        with open(filepath, 'r', encoding='utf-8') as file:
            file_data = file.read()

        # Replace each ID with its corresponding name
        for k, v in sub_to_name.items():
            file_data = file_data.replace(f'"{k}"', f'"{v}"')

        # Write the modified data back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(file_data)
        
        print(f"Processed {filename}")

print("All HTML files have been processed.")