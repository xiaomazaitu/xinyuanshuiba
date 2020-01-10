from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Order,Product,Order_Product,WaterUser
import json
# Create your views here.

def order_list(request):
	if request.method == 'POST':

		json_str = ((request.body).decode('utf-8')) 
		submitdata = json.loads(json_str) 

		username = submitdata['username']
		user = WaterUser.objects.get(userphone = username)
		order_list = Order.objects.filter(user = user)

		print('this get orderlist is {}'.format(order_list))
		ordersArr = []
		for order in order_list:
			order_goods_dic = {'order_id':order.orderid, 'order_money':order.money,'order_time':order.time,'order_phone':order.orderphone}
			order_goods_list = Order_Product.objects.filter(order = order)
			goodsArr = []
			for order_goods in order_goods_list:
				goods_dic = {'name':order_goods.product.name,'ordernum':order_goods.amount}
				goodsArr.append(goods_dic)
			order_goods_dic['goods'] = goodsArr
			ordersArr.append(order_goods_dic)

		jsonData = {'code':'0000','data':ordersArr}
		return JsonResponse(jsonData, safe = False)




	jsonData = {'code':'2000'}
	return JsonResponse(jsonData, safe = False)



def submit_order(request):
	#jsonData = {}
	if request.method == 'POST':

		json_str = ((request.body).decode('utf-8')) 
		submitdata = json.loads(json_str) 

		username = submitdata['username']
		money = submitdata['money']
		user = WaterUser.objects.get(userphone = username)
		address = submitdata['address']
		orderphone = submitdata['phone']
		submit_order = Order(user = user,money = money,address = address, orderphone = orderphone)
		submit_order.save()
		googdsArr = submitdata['goods']
		for goods in googdsArr:
			# print('this order is {}'.format(goods['name']))
			product = Product.objects.get(productid = goods['productid'])
			product.save()
			order = Order_Product(order=submit_order, product = product, amount = goods['ordernum'])
			order.save()
			print('*********************88******************')
			#jsonData['code'] = '0000'


	#print(request.)
	jsonData = {'code':'0000'}
	return JsonResponse(jsonData, safe = False)


		


def water_product(request):

	water_list = Product.objects.all()
	googdsArr = []
	for googds in water_list:
		dic = {'imageUrl':googds.imageUrl,'name':googds.name,'price':googds.price,'ordernum':'0','productid':googds.productid}
		googdsArr.append(dic)
	print(googdsArr)
	data = {'code':'0000','data':googdsArr}
	return JsonResponse(data, safe = False)

	# data = [
	# 	{
	# 		'imageUrl': 'http://127.0.0.1:8000/static/water/nongfushui.jpg',
	# 		'name': '农夫山泉 桶装水 18L',
	# 		'price': '20元',
	# 		'ordernum':'0'
	# 	},
	# 	{
	# 		'imageUrl': 'http://127.0.0.1:8000/static/water/yibaoshui.jpg',
	# 		'name': '怡宝 桶装水 18L',
	# 		'price': '18元',
	# 		'ordernum':'0'
	# 	},
	# 	{
	# 		'imageUrl': 'http://127.0.0.1:8000/static/water/hengdashui.jpg',
	# 		'name': '恒大冰泉 桶装水 18L',
	# 		'price': '30元',
	# 		'ordernum':'0'
	# 	},
	# 	{
	# 		'imageUrl': 'http://127.0.0.1:8000/static/water/quchenshishui.jpg',
	# 		'name': '屈臣氏 桶装水 18L',
	# 		'price': '22元',
	# 		'ordernum':'0'
	# 	},
	# 	{
	# 		'imageUrl': 'http://127.0.0.1:8000/static/water/jingtianshui.jpg',
	# 		'name': '景田 桶装水 18L',
	# 		'price': '20元',
	# 		'ordernum':'0'
	# 	}


	# ]
	# jsonData = {'code':'0000', 'data':data}

	# return JsonResponse(jsonData, safe = False)




def aboutus(request):
	return render(request,'water/aboutus.html')

