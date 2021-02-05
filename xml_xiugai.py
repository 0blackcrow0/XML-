import os
import xml.dom.minidom
import xml.etree.ElementTree



path = r"C:\Users\dell\Desktop\xml/"
files = os.listdir(path)  # 得到文件夹下所有r文件名称
s = []
for xmlFile in files:
    # 遍历文件夹
    portion = os.path.splitext(xmlFile)
    if not os.path.isdir(xmlFile):
        # 判断是否是文件夹,不是文件夹才打开
        # print (xmlFile)

        # xml文件读取操作

        # 将获取的xml文件名送入到dom解析
        dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))
        ###最核心的部分os.path.join(path,xmlFile),路径拼接,输入的是具体路径
        root = dom.documentElement
        #height = root.getElementsByTagName('height')
        #filename=root.getElementsByTagName('filename')

        name=root.getElementsByTagName('name')


        for i in range(len( name )):

            if name[i].firstChild.data == 'scissors' or name[i].firstChild.data == 'scissor':
                name[i].firstChild.data='tool'
            elif    name[i].firstChild.data =='bottle' or name[i].firstChild.data =='coconut_juice' or name[i].firstChild.data =='cola' or name[i].firstChild.data =='water' or name[i].firstChild.data =='alcohol' or name[i].firstChild.data =='coconut juice' or name[i].firstChild.data =='sodas' or name[i].firstChild.data =='juice' or name[i].firstChild.data =='sodas(can)':
                name[i].firstChild.data = 'liquid'

        with open(os.path.join(path, xmlFile), 'w') as fh:
            dom.writexml(fh)
            print('已写入')