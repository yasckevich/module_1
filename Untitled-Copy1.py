#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. У какого фильма из списка самый большой бюджет?

import pandas as pd
data= pd.read_csv('data.csv')

a=data.sort_values(['budget'],ascending=False).head(1)['original_title']
#сортировка по столбцу "бюджет"

display(a)


# In[3]:


#2. Какой из фильмов самый длительный (в минутах)?

data= pd.read_csv('data.csv')

a=data.sort_values(['runtime'],ascending=False).head(1)['original_title']
#сортировка по столбцу "длительность"

display(a)


# In[4]:


#3. Какой из фильмов самый короткий (в минутах)?

data= pd.read_csv('data.csv')

a=data.sort_values(['runtime'],ascending=True).head(1)['original_title']
#сортировка по столбцу "длительность"

display(a)


# In[38]:


#4. Какое число ближе к средней длительности фильма в датасете?

data= pd.read_csv('data.csv')

a=data['runtime']

b=a.describe()
#узнаем среднюю через метод Describe
display(b['mean'])

b=a.mean()
#или узнаем среднюю, запросив напрямую 

display(b)


# In[6]:


#5. Какое число ближе к медианной длительности фильма в датасете?

data= pd.read_csv('data.csv')

a=data['runtime']
b=a.describe()
#узнаем медиану через метод Describe

display(b['50%'])


# In[7]:


#6. Какой самый прибыльный фильм?

data= pd.read_csv('data.csv')
data['profit']=data['revenue']-data['budget']
#создадим новый столбик с данными по прибыли от фильма

a=data.sort_values(['profit'],ascending=False).head(1)['original_title']
display(a)


# In[50]:


#7. Какой фильм самый убыточный?

data= pd.read_csv('data.csv')
data['profit']=data['revenue']-data['budget']
#создадим новый столбик с данными по прибыли от фильма

a=data.sort_values(['profit'],ascending=True).head(1)['original_title']
display(a)


# In[9]:


#8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

data= pd.read_csv('data.csv')
data['profit']=data['revenue']-data['budget']
#создадим новый столбик с данными по прибыли от фильма

a=len(data.query('profit>0'))
print(a)


# In[10]:


#9. Какой фильм оказался самым кассовым в 2008 году?

data= pd.read_csv('data.csv')

a=data.query('release_year==2008')
#сортировка по году

b=a.sort_values(['revenue'],ascending=False).head(1)['original_title']
display(b)


# In[11]:


#10. Какой фильм оказался самым кассовым в 2008 году?

data= pd.read_csv('data.csv')
data['profit']=data['revenue']-data['budget']
#создадим новый столбик с данными по прибыли от фильма

a=data.query('2012<=release_year<=2014')
#сортировка по году

b=a.sort_values(['profit'],ascending=True).head(1)['original_title']
display(b)


# In[12]:


#11. Какого жанра фильмов больше всего?

data= pd.read_csv('data.csv')

a= pd.DataFrame(data.genres.str.split('|').tolist()).stack().value_counts()
a=list(dict(a).keys())
gen=pd.DataFrame(a, columns=['genres'])
#cписок всех жанров

def func(genres):
    a=len(data[data.genres.str.contains(genres)])
    return a
gen['count']=gen.genres.apply(func)
#создаем таблицу с кол-вом фильмов каждого жанра

display(gen.head(1)['genres'])


# In[13]:


#12. Какого жанра среди прибыльных фильмов больше всего?

data= pd.read_csv('data.csv')

data['profit']=data['revenue']-data['budget']
data_new=data.query('profit>0')
#создаем таблицу только с прибыльными фильмами

a=pd.DataFrame(data.genres.str.split('|').tolist()).stack().value_counts()
a=list(dict(a).keys())
gen=pd.DataFrame(a,columns=['genres'])
#cписок всех жанров

def func(genres):
    a=len(data_new[data_new.genres.str.contains(genres)])
    return a
gen['count']=gen.genres.apply(func)
#создаем таблицу с кол-вом фильмов каждого жанра

display(gen.head(1)['genres'])


# In[14]:


#13. Кто из режиссеров снял больше всего фильмов?

data= pd.read_csv('data.csv')

a=data.groupby(['director']).count()
#группировка по режиссеру с количеством фильмов

b=a.sort_values(['original_title'],ascending=False).head(1)['original_title']
display(b)


# In[51]:


#14. Кто из режиссеров снял больше всего прибыльных фильмов?

data= pd.read_csv('data.csv')

data['profit']=data['revenue']-data['budget']
a=data.query('profit>0')
#создаем таблицу только с прибыльными фильмами

b=a.groupby(['director']).count()
#группировка по режиссеру с количеством фильмов

c=b.sort_values(['original_title'],ascending=False).head(1)['original_title']
display(c)


# In[52]:


#15. Кто из режиссеров принес больше всего прибыли?

data= pd.read_csv('data.csv')
data['profit']=data['revenue']-data['budget']
a=data.query('profit>0')
#создаем таблицу только с прибыльными фильмами

b=a.groupby(['director']).sum()
#группировка по режиссеру с суммой по всем столбцам

c=b.sort_values(['profit'],ascending=False).head(1)['profit']
display(c)


# In[53]:


#16. Какой актер принес больше всего прибыли?

data= pd.read_csv('data.csv')

data['profit']=data['revenue']-data['budget']
#создадим новый столбик с данными по прибыли от фильма

a=pd.DataFrame(data.cast.str.split('|').tolist()).stack().value_counts()
new=list(dict(a).keys())
act=pd.DataFrame(new,columns=['actor'])
#создадим таблицу с актерами

def func(acts):
    c=data[data.cast.str.contains(acts)]
    b=c.profit.sum()
    return b
act['profit']=act.actor.apply(func)
#добавим в предыдущую таблицу сумму по прибыли

b=act.sort_values(['profit'],ascending=False).head(1)['actor']
display(b)


# In[18]:


#17. Какой актер принес меньше всего прибыли в 2012 году?

data=pd.read_csv('data.csv')

data=data.query('release_year==2012')
data['profit']=data['revenue']-data['budget']
#создадим новый столбик с данными по прибыли от фильма

a=pd.DataFrame(data_new.cast.str.split('|').tolist()).stack().value_counts()
new=list(dict(a).keys())
act=pd.DataFrame(new,columns=['actor'])
#создадим таблицу с актерами

def func(acts):
    a=data[data.cast.str.contains(acts)]
    b=a.profit.sum()
    return b
act['profit']=act.actor.apply(func)
#добавим в предыдущую таблицу сумму по прибыли

b=act.sort_values(['profit'],ascending=True).head(1)['actor']
display(b)


# In[19]:


#18. Какой актер снялся в большем количестве высокобюджетных фильмов? 

data=pd.read_csv('data.csv')

x=data.budget.mean()
#создаем новую переменную со среднем значением по столбцу "Бюджет"

data_new=data.query('budget> @x')
#создаем новую таблицу только с высокобюджетными фильмами

a=pd.DataFrame(data.cast.str.split('|').tolist()).stack().value_counts()
new=list(dict(a).keys())
act=pd.DataFrame(new,columns=['actor'])
#создаем таблицу с актерами

def func(acts):
    a=len(data_new[data_new.cast.str.contains(acts)])
    return a
act['count']=act.actor.apply(func)
#добавим в предыдущую таблицу количество фильмов по актерам

b=act.sort_values(['count'],ascending=False).head(1)['actor']
display(b)


# In[20]:


#19. В фильмах какого жанра больше всего снимался Nicolas Cage?

data=pd.read_csv('data.csv')

x='Nicolas Cage'
data_new= data[data.cast.str.contains(x)]
#сортируем таблицу только с фильмами с Николасом Кейджем

a=pd.DataFrame(data_new.genres.str.split('|').tolist()).stack().value_counts()
new=list(dict(a).keys())
gen=pd.DataFrame(new,columns=['genres'])
#собираем в таблицу все жанры

def func(gen):
    a=len(data_new[data_new.genres.str.contains(gen)])
    return a
gen['count']=gen.genres.apply(func)
#добавляем в таблицу кол-во фильмов

b=gen.sort_values(['count'],ascending=False).head(1)['genres']
display(b)


# In[21]:


#20. Какая студия сняла больше всего фильмов?

data=pd.read_csv('data.csv')

a=pd.DataFrame(data.production_companies.str.split('|').tolist()).stack().value_counts()
new=list(dict(a).keys())
prod=pd.DataFrame(new,columns=['comp'])
#собираем в таблицу все студии

def func(comp):
    a=len(data[data.production_companies.str.contains(comp)])
    return a
prod['count']=prod.comp.apply(func)
#добавляем в таблицу кол-во фильмов

display(prod.sort_values(['count'],ascending=False).head(1)['comp'])


# In[22]:


#21. Какая студия сняла больше всего фильмов в 2015 году?

data=pd.read_csv('data.csv')
data1=data.query('release_year == 2015')
#сортируем таблицу по году

a=pd.DataFrame(data.production_companies.str.split('|').tolist()).stack().value_counts()
new=list(dict(a).keys())
prod=pd.DataFrame(new,columns=['comp'])
#собираем в таблицу все студии

def func(comp):
    a=len(data1[data1.production_companies.str.contains(comp)])
    return a
prod['count']=prod.comp.apply(func)
#добавляем в таблицу кол-во фильмов

b=prod.sort_values(['count'],ascending=False).head(1)['comp']
display (b)


# In[23]:


#22. Какая студия заработала больше всего денег в жанре комедий за все время?

data=pd.read_csv('data.csv')

data1=data[data.genres.str.contains('Comedy')]
#сортируем таблицу по жанру Комедия

a=pd.DataFrame(data.production_companies.str.split('|').tolist()).stack().value_counts()
new=list(dict(a).keys())
prod=pd.DataFrame(new,columns=['comp'])
#собираем в таблицу все студии

def func(comp):
    a=data1[data1.production_companies.str.contains(comp)]
    b=data1.revenue.sum()
    return b
prod['count']=prod.comp.apply(func)
#добавляем в таблицу сумму по выручке

b=prod.sort_values(['count'],ascending=False).head(1)['comp']
display (b)


# In[24]:


#23. Какая студия заработала больше всего денег в 2012 году?

data1=pd.read_csv('data.csv')

data=data.query('release_year == 2012')
#сортируем таблицу по году

a=pd.DataFrame(data1.production_companies.str.split('|').tolist()).stack().value_counts()
new=list(dict(a).keys())
prod=pd.DataFrame(new,columns=['comp'])
#собираем в таблицу все студии

def func(comp):
    a=data[data.production_companies.str.contains(comp)]
    b=data.revenue.sum()
    return b
prod['count']=prod.comp.apply(func)
#добавляем в таблицу сумму по выручке

b=prod.sort_values(['count'],ascending=False).head(1)['comp']
display (b)


# In[39]:


#24. Самый убыточный фильм от Paramount Pictures?

data=pd.read_csv('data.csv')

data=data[data.production_companies.str.contains('Paramount')]
#сортируем таблицу по нужной студии

data['profit']=data['revenue']-data['budget']
#создадим новый столбик с данными по прибыли от фильма

b=data.sort_values(['profit'],ascending=True).head(1)['original_title']
display (b)


# In[26]:


#25. Какой самый прибыльный год (в какой год студии заработали больше всего)?

data= pd.read_csv('data.csv')
data['profit']=data['revenue']-data['budget']
#создадим новый столбик с данными по прибыли от фильма

b=data.groupby(['release_year']).sum()
#сгруппируем по годам и узнаем сумму по каждому из них

c=b.sort_values(['profit'],ascending=False).head(1)['profit']
display(c)


# In[40]:


#26. Какой самый прибыльный год для студии Warner Bros?

data=pd.read_csv('data.csv')

data=data[data.production_companies.str.contains('Warner Bros')]
#сортируем таблицу по нужной студии

data['profit']=data['revenue']-data['budget']
#создадим новый столбик с данными по прибыли от фильма

a=data.groupby(['release_year']).sum()
#сгруппируем по годам и узнаем сумму по каждому из них

b=a.sort_values(['profit'],ascending=False).head(1)['profit']
display (b)


# In[28]:


#27. В каком месяце за все годы суммарно вышло больше всего фильмов?

data=pd.read_csv('data.csv')

def func(date):
    a=date.find('/')
    b=date[:a]
    return b
data['month']=data.release_date.apply(func)
#создадим отдельный столбик с номером месяца

a=data.groupby(['month']).count()
#группируем таблицу по месяцам

b=a.sort_values(['original_title'],ascending=False).head(1)['original_title']
display(b)


# In[41]:


#28. Сколько суммарно вышло фильмов летом (за июнь, июль, август)?

data=pd.read_csv('data.csv')

def func(date):
    a=date.find('/')
    b=date[:a]
    return int(b)
data['month']=data.release_date.apply(func)
#создадим отдельный столбик с номером месяца

data_new=data.query('5<month<9')
#сортируем таблицу только по летним месяцам

display (len(data_new))


# In[30]:


#29. Какой режиссер выпускает (суммарно по годам) больше всего фильмов зимой?

data=pd.read_csv('data.csv')

def func(date):
    a=date.find('/')
    b=date[:a]
    return int(b)
data['month']=data.release_date.apply(func)
#создадим отдельный столбик с номером месяца

data_new=data.query('month==1 or month==2 or month==12')
#сортируем таблицу только по зимним месяцам

a=data.groupby(['director']).count()
#группируем таблицу по режиссерам

b=a.sort_values(['original_title'],ascending=False)
display(b.head(1)['original_title'])


# In[45]:


#30. Какой месяц чаще всего самый прибыльный в году?

data=pd.read_csv('data.csv')
data['profit']=data['revenue']-data['budget']

def func(date):
    a=date.find('/')
    b=date[:a]
    return int(b)
data['month']=data.release_date.apply(func)
#создадим отдельный столбик с номером месяца

data_new=data.pivot_table(values=['profit'], index=['release_year'], columns=['month'],aggfunc='sum',margins=True)
#создаем сводную таблицу по сумме каждого месяца в каждом году

a=dict(data_new.sum())
new=list(dict(a).values())
df=pd.DataFrame(new, columns=['sum'],index=['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь','All'])
#создаем таблицу с суммой по каждому месяцу и назваию месяца

print(df.sort_values(['sum'],ascending=False).head(2))


# In[32]:


#31. Названия фильмов какой студии в среднем самые длинные по количеству символов?

data=pd.read_csv('data.csv')

a=pd.DataFrame(data.production_companies.str.split('|').tolist()).stack().value_counts()
new=list(dict(a).keys())
prod=pd.DataFrame(new,columns=['comp'],index=new)
#собираем в таблицу все студии

def func(comp):
    a=data[data.production_companies.str.contains(comp)]
    b=a['original_title']
    return list(b)
prod['film']=prod.comp.apply(func)
#добавляем в таблицу названия фильмов по каждой студии

def func(word): 
    s=len(word)
    return s
prod['len']=prod.film.apply(func)
#добавляем в таблицу количество фильмов по каждой студии

def func(letter):
    a=str(letter)
    b=a.count(' ')
    c=a.count('[')
    d=a.count(']')
    e=a.count(',')
    f=a.count('-')  
    s=len(letter)*2
    z=len(a)-b-c-d-e-f-s
    return z
prod['letter']=prod.film.apply(func)
#добавляем в таблицу количество символов в фильмах по каждой студии (чувствую, что эту часть можно сделать гораздо проще, мб с помощью регулярных выражений)

prod['mean']=prod['letter']/prod['len']
#добавляем в таблицу среднее количество символов в названии фильмах по каждой студии

print (display(prod.sort_values(['mean'],ascending=False).head(1)['comp']))


# In[33]:


#32. Названия фильмов какой студии в среднем самые длинные по количеству слов?

import pandas as pd
data=pd.read_csv('data.csv')

a=pd.DataFrame(data.production_companies.str.split('|').tolist()).stack().value_counts()
new=list(dict(a).keys())
prod=pd.DataFrame(new,columns=['comp'],index=new)
#собираем в таблицу все студии

def func(comp):
    a=data[data.production_companies.str.contains(comp)]
    b=a['original_title']
    return list(b)
prod['film']=prod.comp.apply(func)
#добавляем в таблицу названия фильмов по каждой студии

def func(word): 
    s=len(word)
    return s
prod['len']=prod.film.apply(func)
#добавляем в таблицу количество фильмов по каждой студии

def func(word):
    a=str(word)
    b=a.count(' ')+1
    return b
prod['word']=prod.film.apply(func)
#добавляем в таблицу количество слов в названиях фильмов по каждой студии. (Считаем кол-во пробелов и добавляем 1, так как одно слово всегда остается без пробела)

prod['mean']=prod['word']/prod['len']
prod=prod.query('len>0')
#узнаем среднее кол-во слов

print (display(prod.sort_values(['mean'],ascending=False).head(1)['comp']))


# In[34]:


#33. Сколько разных слов используется в названиях фильмов (без учета регистра)?


import pandas as pd
data=pd.read_csv('data.csv')

a=pd.DataFrame(data.original_title.str.split('|').tolist()).stack().value_counts()
#создаем список всех названий 

new=str(list(dict(a).keys())).replace(',','')
new=new.replace("'",' ')
new=new.replace('"',' ')
new=new.replace('[',' ')
new=new.replace(']',' ')
new=new.replace(':',' ')
new=new.replace('-',' ')
new=new.replace('/',' ')
new=new.replace('&',' ')
new=new.replace('1','')
new=new.replace('2','')
new=new.replace('3','')
new=new.replace('4','')
new=new.replace('5','')
new=new.replace('6','')
new=new.replace('7','')
new=new.replace('8','')
new=new.replace('9','')
new=new.replace('0','')
new=new.replace('.',' ')
new=new.replace(')',' ')
new=new.replace('(',' ')
new=new.replace('!','')
new=new.replace('?','')
#убираем лишние знаки (чувствую, что эту часть можно сделать гораздо проще, мб с помощью регулярных выражений)

new=new.lower()
#ставим один регистр по всем словам 

new=new.split(' ')
#делаем список слов 

unique=[]
for i in new:
    if i not in unique:
        unique.append(i)
#составляем список уникальных значений

print(len(unique))


# In[35]:


#34. Какие фильмы входят в 1 % лучших по рейтингу?

import pandas as pd
data=pd.read_csv('data.csv')

data_new=data['vote_average']
import numpy as np
a=np.percentile(data_new, 99)
#узнаем границу 1%

data=data.query('vote_average> @a')
print(display(data))


# In[59]:


#36. Какие актеры чаще всего снимаются в одном фильме вместе?

#тут я не смогла додуматься как сделать

import pandas as pd
import itertools

data=pd.read_csv('data.csv')
a=pd.DataFrame(data.cast.str.split('|').tolist()).stack().value_counts()
new=list(dict(a).keys())
#создала список со всеми актерами

a=list(itertools.combinations(new,2))
#все возможные комбинации актеров 

#но далее возникла ошибка: 
#IOPub data rate exceeded.
#The notebook server will temporarily stop sending output
#to the client in order to avoid crashing it.
#To change this limit, set the config variable
#`--NotebookApp.iopub_data_rate_limit`.

#Current values:
#NotebookApp.iopub_data_rate_limit=1000000.0 (bytes/sec)
#NotebookApp.rate_limit_window=3.0 (secs)"

#по идее дальше нужно перебрать какие пары сколько раз встречались, отфильтровать и найти лидера
#но нет(

#поэтому пришлось вручную перебирать
data=pd.read_csv('data.csv')

data1=data[data.cast.str.contains('Johnny Depp')]
data1=data1[data.cast.str.contains('Helena Bonham')]
print('Johnny Depp and Helena Bonham Carter', len(data1))

data2=data[data.cast.str.contains('Hugh Jackman')]
data2=data2[data.cast.str.contains('Ian McKellen')]
print('Hugh Jackman and Ian McKellen', len(data2))

data3=data[data.cast.str.contains('Vin Diesel')]
data3=data3[data.cast.str.contains('Paul Walker')]
print('Vin Diesel and Paul Walker', len(data3))

data4=data[data.cast.str.contains('Adam Sandler')]
data4=data4[data.cast.str.contains('Kevin James')]
print('Adam Sandler and Kevin James', len(data4))

data5=data[data.cast.str.contains('Daniel Radcliffe')]
data5=data5[data.cast.str.contains('Rupert Grint')]
print('Daniel Radcliffe and Rupert Grint', len(data5))
print(a)    


# In[54]:


#36. У какого из режиссеров самый высокий процент фильмов со сборами выше бюджета?

import pandas as pd

data=pd.read_csv('data.csv')

a=data.groupby(['director']).count()
a=a[['revenue']]
#группируем таблицу по режиссеру с общим кол-вом фильмов

data_new=data.copy()
data_new['profit']=data['revenue']-data['budget']
data_new=data_new.query('profit>0')
b=data_new.groupby(['director']).count()
b=b[['profit']]
#группируем таблицу по режиссеру с кол-вом прибыльных фильмов

c=pd.concat([a,b],axis=1)
#объединяем таблицу

c = c.fillna(0) 
#приравниваем ошибку к нулю

def func(profit):
    a=int(profit)
    return a
c['profit']=c.profit.apply(func)
#приводим столбец к цифровому значению

c['e']=c['profit']/c['revenue']
#узнаем % фильмов со сборами выше бюджета

a=c['e']['Quentin Tarantino']*100
print('Quentin Tarantino', a, '%')
a=c['e']['Steven Soderbergh']*100
print('Steven Soderbergh', a, '%')
a=c['e']['Robert Rodriguez']*100
print('Robert Rodriguez', a, '%')
a=c['e']['Christopher Nolan']*100
print('Christopher Nolan', a, '%')
a=c['e']['Clint Eastwood']*100
print('Clint Eastwood', a, '%')

#почему-то два правильных ответа, ошибку не смогла найти


# In[ ]:


#небольшой эпилог:
#да, я все никак не освою github, его логику поняла, а механику - нет. на сл неделю буду исправляться
#не хватает понимания где можно использовать регулярные выражения, 
#вроде штука крутая, а с пониманием где его лучше употреблять и как - проблемы
#и еще вопрос: как лучше всего работать с ошибками и как их "читать"?

