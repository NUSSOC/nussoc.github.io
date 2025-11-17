import os
import sys
import re

# --- CONFIGURATION ---
# This is the list of directories *relative to this script*.
# This script assumes you are running it from the '2510' folder.
directories_to_process = ['.', 'games/qual_1', 'games/qual_2', 'games/qual_3', 'games/qual_4', 'games/qual_5', 'games/finals']

# This is the map you generated
sub_to_name = {
    "2610514": "Aaron Tan Wei Heng",
    "2612074": "Adam Yap Wenbin",
    "2613730": "Aditya Purushottam Naik",
    "2614874": "Ameera D/O Mohamed Safi",
    "2613047": "Ashley Emma Tan",
    "2614692": "Ashlyn Lim",
    "2619759": "Azka Tazkiatunnafsi",
    "2613936": "Bansal Prisha",
    "2611380": "Benjamin Jieming Phua",
    "2612968": "Brenda Lau Zhuo Min",
    "2614318": "Bryan Lei Heng Yi",
    "2606975": "Chan Jun Jie",
    "2615449": "Cheang Xi Ning Janelle",
    "2615206": "Chen Yun Xin, Aliz",
    "2613928": "Cheng Ruiyan",
    "2613018": "Chew An Jie",
    "2608692": "Chew Rui Qi Chloe",
    "2609423": "Chia Loke En, Lu-Anne",
    "2614240": "Chin Weng Hong",
    "2615773": "Chiu Lai Hou, Leo",
    "2614204": "Chiu Qi Yang",
    "2612736": "Chloe Wong Hui Xin",
    "2625383": "Chong Zhong Wei",
    "2609315": "Chu Ruoyuan",
    "2605278": "Chua Cheng Hao",
    "2616668": "Chua Jun En",
    "2606494": "Chua Lu Teng, Lorraine",
    "2611182": "Chua Ya Wen",
    "2619418": "Dani Goh",
    "2599113": "Danven Ong Wei Dong",
    "2604451": "Darren Chua Ming Zhe",
    "2602728": "Daryl Ke Gut Jun",
    "2613113": "Devireddy Poorvek Reddy",
    "2613467": "Do Thien Phuc",
    "2605017": "Dominic Bryan",
    "2612327": "Dylan Long Kai Xi @ Tian Cheng",
    "2610291": "Elvis Foo Shun Han",
    "2621432": "Eng Li Hui Grace",
    "2613565": "Fang Chenyu",
    "2611634": "Feliciano Margaret Elisha Fontanilla",
    "2610904": "Foong Kaixuan, Julia",
    "2609332": "Fung Zhuowen",
    "2612087": "Gerome Teo Yi Xun",
    "2609645": "Glenda Han Shi Jia",
    "2599395": "He Qingya",
    "2603917": "Heng Kaiyi",
    "2610007": "Heng Theng Wei",
    "2607889": "Hong Yen Xiang Gremio",
    "2613168": "Hu Jiaxin",
    "2612792": "Huang Yifan",
    "2615200": "Ian Liew Wen-Hao",
    "2613069": "Iizen Sng Lik Tiah",
    "2599295": "Imelda Chen",
    "2605969": "Jason Seah Chee Yang",
    "2613630": "Jayden Sim Xun",
    "2612671": "Jeffrey Tiang Jun Rong",
    "2618597": "Jeon Gahyeon",
    "2620168": "Jeyaraj Justin",
    "2613278": "Ji Zhihang",
    "2616705": "Joel Goh Min Feng",
    "2624692": "Jordan Ng Ruiyi",
    "2611017": "Justin Stevenson Theodorus",
    "2600740": "Kabir Durgani",
    "2619057": "Katharina Juliani",
    "2622581": "Keri-Ann Shi",
    "2612237": "Khew Chervei",
    "2612468": "Koh Shun Yi Audrey",
    "2613304": "Kwang Le Ping Sharyl",
    "2621428": "Lai Jun Xing Benjamin",
    "2616428": "Le Huynh Phuong Truc",
    "2612754": "Lee Chin Yi",
    "2608123": "Lee En, Randall",
    "2609368": "Lee Yu Xuan Ronald",
    "2604901": "Leong Jun Hao",
    "2608822": "Leong Kai Jie",
    "2609297": "Li Fucheng",
    "2608050": "Li Xueyi Joanne",
    "2610133": "Lim Jia Tzer",
    "2620480": "Lim Jin Xin Hannah",
    "2613442": "Lim Ray Hing",
    "2612012": "Lim Siew Woo",
    "2612319": "Lim Tze Yen Ashleigh",
    "2510133": "Lim Wei Jie, Eugene",
    "2623675": "Lim Yonghui",
    "2617701": "Lim Yuan Qing",
    "2609560": "Lim Zhi Yi, Mariel",
    "2613820": "Loh Jing Jie, Aloysius",
    "2612735": "Loh Wei Xuan",
    "2609557": "Low Kah Xin Kennice",
    "2611724": "Loy Liang Yi",
    "2613167": "Megan Lim Fang Hui",
    "2620449": "Muhammad Haziq Bin Noorazmi",
    "2611529": "Muhammad Waseem Akram Amanullah",
    "2615454": "Ng Sher Lyn",
    "2613789": "Ng Shi Jia",
    "2610058": "Ng Wei Hao, Danson",
    "2609379": "Ng Wei Xun Bradley",
    "2608764": "Ng Yu Yang",
    "2612207": "Ngo Duc Nhat Minh",
    "2607157": "Nicholas Chang Tian Rong",
    "2605866": "Nicholas Saw Ju Meng",
    "2614947": "Nigel Chung Yok Kai",
    "2610835": "Ong Jing Da",
    "2607078": "Phang Wei Yan Jolyn",
    "2610196": "Quek Jin Kai",
    "2626353": "Reine Tan Si Jie",
    "2611508": "Rohan Varatharajan",
    "2598318": "Rossa Joann Lu Si Yun",
    "2613201": "Sakshi Vashist",
    "2612138": "Sean Chua Kai Jun",
    "2618839": "Shanyce Goh",
    "2624718": "Shuen Yong Lok Caleb",
    "2612498": "Siah Kai Jin",
    "2610243": "Soh Shi Huan",
    "2611694": "Sun Jianxiang",
    "2611427": "Tan Chern Yu Ryan",
    "2611979": "Tan Hui Shi",
    "2610619": "Tan Jeng Khiang Damien",
    "2613101": "Tan Jie Yin Elicia",
    "2605160": "Tan Lay How Caleb",
    "2614923": "Tan Rui Teng",
    "2615821": "Tan Sing Kuang",
    "2626836": "Tan Yi Hao",
    "2607595": "Tan Zhi Xian Kane",
    "2612216": "Tang Yu Ying, Valerie",
    "2600279": "Tay Jyun Wey",
    "2606633": "Tay Klodia",
    "2613435": "Teh Kah Wah",
    "2618377": "Teo Choon Pin",
    "2604290": "Teo Qi En Tricia",
    "2615475": "Teo Wei Hng Ryan",
    "2614699": "Thivakolrakot Krittnicha",
    "2570663": "Timothy Lee",
    "2610705": "Tse Min Jia",
    "2624017": "Umashankar Suhas",
    "2599858": "Valmonte Janelle Darcy Juban",
    "2611939": "Vera Lye Jing Ting",
    "2587739": "Vera Tay Xiang Yu",
    "2613351": "Wang Heyueyang",
    "2613784": "Wei Leyang Fiona",
    "2615855": "Wong Jae En,Kadyne",
    "2614985": "Woo Yu Xin",
    "2616141": "Wu Chengye",
    "2605623": "Wu Qibing",
    "2612843": "Xu Qingyang",
    "2612109": "Yang Hanming",
    "2617359": "Yang Siyu Ivy",
    "2609644": "Yap Thiam Lok Keith",
    "2608603": "Yeo Chang Long, Jeryl",
    "2624234": "Yim Wei Jie Dylan",
    "2599539": "Yong Koon Yu",
    "2606661": "Yong Man Ting",
    "2605052": "Zachary Ong Ze En",
    "2613317": "Zheng Jia"
}
# --- END CONFIGURATION ---

# Sort keys by length, descending, to avoid partial matches
# (e.g., "260" replacing part of "2609315")
sorted_keys = sorted(sub_to_name.keys(), key=len, reverse=True)

print("--- Replacing content in all HTML files ---")
# This script will replace content in all files, but will not rename them.
for directory in directories_to_process:
    print(f"Processing directory: {directory}")
    try:
        # Check if the path is a valid directory
        if not os.path.isdir(directory):
            print(f"Skipping '{directory}' as it is not a directory.")
            continue
            
        for filename in os.listdir(directory):
            if filename.endswith('.html'):
                filepath = os.path.join(directory, filename)
                
                # Read the HTML file
                try:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        file_data = file.read()
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
                    continue
                
                new_file_data = file_data
                
                # Replace each ID with its corresponding full name
                # This is a much safer replacement logic based on the HTML
                # you provided.
                for k in sorted_keys: 
                    v = sub_to_name[k]
                    
                    # Target 1: For index.html (winners)
                    # <strong>2611634</strong> -> <strong>Feliciano...</strong>
                    new_file_data = new_file_data.replace(f'<strong>{k}</strong>', f'<strong>{v}</strong>')

                    # Target 2: For index.html (losers)
                    # <li>2613113</li> -> <li>Devireddy...</li>
                    new_file_data = new_file_data.replace(f'<li>{k}</li>', f'<li>{v}</li>')

                    # Target 3: For game-log.html (Overview table winners)
                    # <th><i class="fa fa-trophy"></i> 2599858</th> -> <th><i class="fa fa-trophy"></i> Valmonte...</th>
                    new_file_data = new_file_data.replace(f'<th><i class="fa fa-trophy"></i> {k}</th>', f'<th><i class="fa fa-trophy"></i> {v}</th>')

                    # Target 4: For game-log.html (Overview table others)
                    # <th>2611017</th> -> <th>Justin...</th>
                    new_file_data = new_file_data.replace(f'<th>{k}</th>', f'<th>{v}</th>')

                    # Target 5: For game-log.html (Scores sidebar)
                    # <td>2609644</td> -> <td>Yap Thiam Lok Keith</td>
                    new_file_data = new_file_data.replace(f'<td>{k}</td>', f'<td>{v}</td>')

                    # Target 6: For game-log.html (Event log spans)
                    # class="game-object">2609423</span> -> class="game-object">Chia Loke En, Lu-Anne</span>
                    new_file_data = new_file_data.replace(f'class="game-object">{k}</span>', f'class="game-object">{v}</span>')

                # Write the modified data back to the file
                # Only write if changes were actually made
                if new_file_data != file_data:
                    try:
                        with open(filepath, 'w', encoding='utf-8') as file:
                            file.write(new_file_data)
                        print(f"  Updated content for: {filename}")
                    except Exception as e:
                        print(f"  Error writing {filepath}: {e}")
                else:
                    # This check is useful to see if the script is finding the files
                    # but not finding any matching patterns.
                    if filename != "index.html": # index.html links are expected to change
                        print(f"  No display IDs found to replace in: {filename}")

    except FileNotFoundError:
        print(f"ERROR: Directory not found: '{directory}'. Skipping.")
    except Exception as e:
        print(f"An unexpected error occurred in {directory}: {e}")

print("\n--- All files processed ---")