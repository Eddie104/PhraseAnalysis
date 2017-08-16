#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jieba
import jieba.analyse
import argparse
import os
from pyecharts import Bar
from pyecharts import Pie

def extract_tags(content):
	# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
	# print("Full Mode: " + "/ ".join(seg_list))
	tags = jieba.analyse.extract_tags(content, topK=20, withWeight=True, allowPOS=())
	phrase = []
	weight = []
	for tag in tags:
		phrase.append(tag[0])
		weight.append(tag[1])
	return phrase, weight

def renderChart(phrase, weight):
	# bar = Bar("热词图", "出现频率最高的词")
	# bar.add("", phrase, weight, xaxis_name="词语", yaxis_name="权重", is_xaxislabel_align=False, xaxis_interval=0)
	# # bar.show_config()
	# bar.render()
	pie = Pie("热词图", title_pos='center')
	pie.add("", phrase, weight, radius=[40, 75], label_text_color=None, is_label_show=True, legend_orient='vertical', legend_pos='left')
	# pie.show_config()
	pie.render()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("txt", help = "the path of txt")
	options = parser.parse_args()

	txtPath = options.txt;
	if os.path.exists(txtPath):
		f = open(txtPath, 'br')
		txt = f.read()
		f.close()

		phrase, weight = extract_tags(txt)
		renderChart(phrase, weight)
	else:
		print('{} is not existed'.format(txtPath))