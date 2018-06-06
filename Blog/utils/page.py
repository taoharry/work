#!usr/bin/env python
# coding:utf-8

def shut_page_content(number,lt):
	#未使用
	newlt = []
	number = int(number)
	longer = len(lt)
	l = (number-1)*5
	r = number *5

	if l<longer < r :
		r = longer
	if number ==1:
		for i in range(0, 5):
			newlt.append(lt[i])
	else:
		for i in range(l,r):

			newlt.append(lt[i])
	return newlt

def all_page(long,shutnum):
	#实现总条数转化为页数功能
	n = divmod(long, shutnum)
	if n[1] != 0:
		longer = n[0] + 1
	else:
		longer = n[0]
	return longer



def page_list(all_page,select_page):
	#实现页脚切分也功能

	select_page = abs(int(select_page))
	r = select_page + 2
	l = select_page - 2
	if 0 < select_page <= 5:
		if 0 < all_page <= 5:
			list_page = range_page_list(0, all_page)
		else:
			list_page = range_page_list(0,select_page)

	elif  select_page <= all_page :
		if r < all_page:
			list_page = range_page_list(l, r)
		elif select_page <= all_page <= r:
			list_page = range_page_list(l, all_page)

	else:
		if select_page > all_page:
			if 0< all_page <= 5:
				list_page = range_page_list(0, all_page)
			else:
				list_page = range_page_list(all_page-2, all_page+2)
	newlt = []
	for i in list_page:
		i = i+1
		newlt.append(i)

	return newlt

def range_page_list(l,r):
	lt = []
	for i in range(l,r):
		lt.append(i)
	return lt