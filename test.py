mydict = {'key1':{ 'KeyinKey': {
    'InsideKey1' : 'Value1',
    'InsideKey2' : 'Value2',
    'InsideKey3' : 'Value3'
}}}

for key in mydict['key1']['KeyinKey']:
    print (key)