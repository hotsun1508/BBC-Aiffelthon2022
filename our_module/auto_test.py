# -*- coding: utf-8 -*-
"""auto_test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oX4sTgZqJF2Huqwr6LkPBLu8KxhKUwBs
"""

from collections import Counter
import pandas as pd
import gensim
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

class get_detail_plot:
    def __init__(self, memo_data):
        self.memo_data = memo_data
        sub_type_list = list(memo_data['lesion_sub_type'].unique())
        self.sub_type_list = sub_type_list
        
    def get_detail_dict(self):
        
        type_dict_detail = {}
        for i in range(len(self.memo_data)):
            if self.memo_data['lesion_sub_type'][i] in type_dict_detail.keys():
                if self.memo_data['lesion_detail_type'][i] in type_dict_detail[self.memo_data['lesion_sub_type'][i]]:
                    continue
                else:
                    type_dict_detail[self.memo_data['lesion_sub_type'][i]].append(self.memo_data['lesion_detail_type'][i])
            else:
                type_dict_detail[self.memo_data['lesion_sub_type'][i]] = [self.memo_data['lesion_detail_type'][i]]

        return type_dict_detail
    
    def get_sub_type_plot(self):
        uq_id_list = list(self.memo_data['lesion_id'].unique())

        uq_id_index = []
        for i in range(len(uq_id_list)):
            uq_id_index.append(self.memo_data.index[self.memo_data['lesion_id']== uq_id_list[i]][0])


        sub_type_count = []
        for n, i in enumerate(self.sub_type_list):
            sub_type_count.append(0)
            for j in uq_id_index:
                if self.memo_data['lesion_sub_type'][j] == i:
                    sub_type_count[n] += 1


        ty_plt_dict = {}
        temp_idx = []
        for i in range(len(self.sub_type_list)):
            ty_plt_dict[self.sub_type_list[i]] = sub_type_count[i]
            temp_idx.append(i)
            ty_plt_df = pd.DataFrame(ty_plt_dict,index = [0])
            ty_plt_df = ty_plt_df.transpose()
            ty_plt_df = ty_plt_df[0].sort_values(ascending = True)
            ty_plt_df

        x_lo = temp_idx
        x = list(ty_plt_df.index)
        y = list(ty_plt_df.values)
        plt.figure(figsize=(14,10))
        plt.title('sub_type_count')
        plt.barh(x, y, label = 'sub_type_count')

        for i, v in enumerate(y):
            plt.text(v, x_lo[i], y[i],
                    fontsize = 14,
                    color = 'blue')
            
        # plt.xticks(rotation=90)
        plt.xlabel('?????? ??????')
        plt.legend()
        plt.grid()

        plt.show()
            
    def get_detail_type_plot(self):
        ## sub_type ?????? ??????
        # temp_num = int(input('[1]: ????????????\t [2]: ????????????\t [3]: ?????????\t [4]: ?????????\n[5]: ?????????\t [6]: ????????????\t [7]: ??????\t [8]: ????????????\n[9]: ????????????\t [10]: ????????????\t [11]: ???????????????\t [12]: ??????/????????????\n[13]: ????????????\t [14]: ???????????????\t [15]: ????????????\t [16]: ????????????\n[17]: ?????????\t [18]: ?????????\t [19]: ?????????\t [20]: ADAS\n[21]:????????? ??????\n'))
        # search = le_sub_ty[temp_num-1]
        temp_num = int(input('[1]: ????????????(1???)\t [2]: ????????????(4???)\t [3]: ?????????(8???)\t [4]: ?????????(14???)\n[5]: ?????????(2???)\t [6]: ????????????(8???)\t [7]: ??????(5???)\t\t [8]: ????????????(8???)\n[9]: ????????????(30???)\t [10]: ????????????(4???)\t [11]: ???????????????(7???)\t [12]: ??????/????????????(7???)\n[13]: ????????????(5???)\t [14]: ???????????????(2???)\t [15]: ????????????(1???)\t [16]: ????????????(27???)\n[17]: ?????????(6???)\t [18]: ?????????(6???)\t [19]: ?????????(3???)\t [20]: ADAS(2???)\n[21]:????????? ??????(1???)\n'))
        search = self.sub_type_list[temp_num-1]

        ##??????
        detail_dict = self.get_detail_dict()
        detail_list = detail_dict[search] # ????????? ??????

        temp_df = self.memo_data.loc[self.memo_data['lesion_sub_type']== search] # sub_type??? ???????????? df

        # ??????id??? ??????
        temp_df_drop_index = []
        temp_df_keep_id = []
        for i in range(len(temp_df)):
            if temp_df['lesion_id'][temp_df.index[i]] in temp_df_keep_id:
                temp_df_drop_index.append(temp_df.index[i])
            else:
                temp_df_keep_id.append(temp_df['lesion_id'][temp_df.index[i]])

        temp_df = temp_df.drop(index = temp_df_drop_index, axis = 0, inplace = False)

        # ??????id?????? detail ?????? count
        temp_detail_count = []
        for n, i in enumerate(detail_list):
            temp_detail_count.append(0)
            for j in temp_df.index:
                if temp_df['lesion_detail_type'][j] == i:
                    temp_detail_count[n] += 1

        # ???????????? ????????? ?????? df ??????
        temp_plt_dict = {}
        temp_idx2 = []
        for i in range(len(detail_list)):
            temp_plt_dict[detail_list[i]] = temp_detail_count[i]
            temp_idx2.append(i)
        temp_plt_df = pd.DataFrame(temp_plt_dict,index = [0])
        temp_plt_df = temp_plt_df.transpose()
        temp_plt_df = temp_plt_df[0].sort_values(ascending = True)
        # temp_plt_df


        # ????????? ?????????
        x_lo2 = temp_idx2
        x_2 = list(temp_plt_df.index)
        y_2 = list(temp_plt_df.values)
        plt.figure(figsize=(14,10))
        plt.title(search)
        plt.barh(x_2, y_2, label = 'detail_type_count')

        for i, v in enumerate(y_2):
            plt.text(v, x_lo2[i], y_2[i],
                    fontsize = 14,
                    color = 'blue')
            
        # plt.xticks(rotation=90)
        plt.xlabel('?????? ??????')
        plt.legend()
        plt.grid()

        return(plt.show())

