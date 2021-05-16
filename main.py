import csv

path = './heroes_information.csv'

with open(path, mode='r', encoding='shift_jis') as file:
    reader = csv.reader(file)

    csv_list = []

    #csv_listにcsvファイルを順番に全部入れる
    for row in reader:
        csv_list.append(row)

    #new_csv_listに上から10列入れる 　0列目は入れない
    new_csv_list = csv_list[1:11]


    with open('new_hero.csv', mode='w',newline='', encoding='shift_jis') as new_file:
        writer = csv.writer(new_file)
        #一行目に入るタイトル的なやつ
        writer.writerow(["名前", "性別", "身長（2倍）"])

        for line in new_csv_list:

            #身長を2倍にする
            height_double = int(line[6]) * 2
        
            #名前と性別と倍にした身長を表示　他は割愛
            writer.writerow([line[1],line[2], int(height_double)])
            

