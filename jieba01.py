import jieba
import jieba.analyse


text = '總統蔡英文論文風波延燒後，最新民調今日出爐！據親藍民調公布結果，蔡英文支持度45%，遙遙領先韓國瑜的33%，兩人差距擴大到12個百分點。顯示論文門風波，並未重創小英聲望。'
tags = jieba.analyse.extract_tags(text, topK=5)  
#topK 為返回幾個TF/IDF 權重最大的關鍵詞，默認值為20
print(tags)