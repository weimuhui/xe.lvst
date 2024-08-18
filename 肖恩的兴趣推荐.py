'''我的主页'''
import streamlit as st
from PIL import Image




page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '勾选框','跳转页面','我的留言区'])

def page_1():
    st.write('''肖恩的兴趣推荐''')
    with open('cjh.mp3','rb') as f:
            mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    tab1,tab2,tab3,tab4 = st.tabs(['电影','游戏','书籍','习题'])
    with tab1:
        st.image('长津湖.jpeg')
        st.write('肖恩的电影推荐：')
        st.write('<<长津湖>>')
    with tab2:
        with open('aqtwzq.mp3','rb') as f:
            mymp3=f.read()
        st.audio(mymp3,format='audio/mp3',start_time=0)
        st.image('暗区突围.jpg')
        st.write('肖恩的游戏推荐：')
        st.write('暗区突围')
    with tab3:
        st.image('特种兵学校.jpg')
        st.image('少年特战队.jpg')
        st.write('肖恩的书籍推荐：')
        st.write('特种兵学校')
        st.write('少年特战队')
        st.write('（特别好看）')
    with tab4:
        st.write('肖恩的习题推荐：')
        st.write('万唯')

def page_2():
    '''我的图片处理工具'''
    tab1,tab2,tab3,tab4,tab5 = st.tabs(['原图','旋转','黑白','缩放','改色'])
    st.write('sunglasses:图片处理小程序:sunglasses:')
    uploaded_file = st.file_uploader('上传图片',type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_rotate(img))
        with tab3:
            st.image(img_black(img))
        with tab4:
            st.image(img_resize(img))
        with tab5:
            st.image(img_change(img,0,1,2))

def img_rotate(img):
    angle = st.number_input('请输入要旋转的角度',value = 90)
    if angle != '':
        angle = int(angle)
        img_change1 = img.rotate(angle)
        return img_change1

def img_resize(img):
    big = st.number_input('请输入图片尺寸',value = 200)
    if big != '':
        big=int(big)
        img_change2 = img.resize((big,big))
        return img_change2

def img_black(img):
    img_change3 = img.convert('L')
    return img_change3     

def img_change(img,rc,gc,bc):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y] [rc]
            g = img_array[x,y] [gc]
            b = img_array[x,y] [bc]
            img_array[x,y] = (r,g,b)
    return img

def page_3():
    '''我的智能词典'''
    st.write('智慧词典')
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list=f.read().split('\n')

    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')

    words_dict={}        
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
        
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list=f.read().split('\n')

    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')

    times_dict={}        
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    
    word = st.text_input('请输入要查询的单词')

    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict :
            times_dict[n]+=1
        else:
            times_dict[n] = 1

        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message = ''
            for k,v in times_dict.items():
                message += str(k) + '#' + str(v) + '/n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：',times_dict[n])
        if word == 'balloon':
            st.snow()
            st.write('咋么肥是')
def page_4():
    '''勾选框'''
    cb = st.checkbox('勾选选项')
    if cb:
        st.write('选项被勾选', cb)
    
    st.write('----')
    st.write('你知道吗：为什么要设置公网和私网？为什么不让每一个设备都直接连接到公网上？')
    cb1 = st.checkbox('易于管理')
    cb2 = st.checkbox('效率高')
    cb3 = st.checkbox('网速快')
    cb4 = st.checkbox('安全性好')
    l = [cb1, cb2, cb3, cb4]
    if st.button('确认答案'):
        if True in l:
            st.write('其实都不对，答案是“历史问题，不得已而为之”')
        else:
            st.write('好厉害！确实都不对，真实答案是“历史问题，不得已而为之”.')

def page_5():
    '''跳转页面'''
    st.link_button('百度首页', 'https://www.baidu.com/')
    st.write('这是我们的主网页，其他的在下面')
    st.write('----')
    go = st.selectbox('选择想要查看的网页', ['百度', 'bilibili'])
    if go == '百度':
        st.link_button('跳转到'+go,'https://www.baidu.com/' )
    elif go == 'bilibili':
        st.link_button('跳转到'+go, 'https://www.bilibili.com/')

def page_6():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('/n')
    for i in range(len(messages_list)):  
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        with st.chat_message('😀'):
            st.write(i[1],':',i[2])
    name = st.text_input('留言人姓名：')
    new_message = st.text_input('想要说的话：')

    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2]  + '/n'
            message = message[:-1]
            f.write(message)
    st.write('先写留言人姓名，再写想要说的话。点‘‘留言’’，按刷新键，就能获得最新的留言啦！')

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '跳转页面':
    page_5()
elif page == '勾选框':
    page_6()