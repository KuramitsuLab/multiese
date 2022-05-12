import csv
import sys
import black
import Levenshtein
from nltk import bleu_score
from rouge import Rouge

def read_tsv(filename, index=2, pred_index=1):
    ss = []
    with open(filename) as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            ss.append((row[index], row[pred_index]))
    return ss


def Exact_Match(ss):
  
  #正答数
  correct=0

  #blackが使用できない数
  black_NG=0

  for line in ss:
    index=line[0]
    pred=line[1]

    try:
      pred_black=black.format_str(pred,mode=black.Mode())[:-1]

      if index==pred_black:
        correct+=1

    except:
      black_NG+=1
      #blackを利用した際にERRORが発生した箇所をテキストファイルに記入
      with open('BLACK_NG.txt',mode='a') as f:
        f.writelines(line)
        f.write('\n')

  #誤答数
  no_correct=len(ss)-correct

  #正答率
  correct_answer_rate=correct/len(ss)

  print("全体件数：",len(ss))
  print("BLACK_NG：",black_NG)
  print("正答数：",correct)
  print("誤答数：",no_correct)
  print("正答率：",correct_answer_rate)


def Levenstein(ss):
  
  #合計
  sum_Levenstein=0

  for line in ss:
    index=line[0]
    pred=line[1]
    sum_Levenstein += Levenshtein.ratio(index,pred)

  #平均値
  leven=sum_Levenstein/len(ss)
  
  print("leven：",leven)


#警告あり
def BLEU1(ss):

  #合計
  sum_bleu1 = 0

  for line in ss:
    index=line[0]
    pred=line[1]
    
    sum_bleu1 += bleu_score.sentence_bleu(index,pred)

  #平均値
  bleu1 = sum_bleu1 / len(ss)

  print("BLEU1：",bleu1)


#警告なし
def BLEU2(ss):

  #合計
  sum_bleu2 = 0

  for line in ss:
    index=line[0]
    pred=line[1]
    
    sum_bleu2 += bleu_score.sentence_bleu(index,pred,smoothing_function=bleu_score.SmoothingFunction().method2)

  #平均値
  bleu2 = sum_bleu2 / len(ss)

  print("BLEU2：",bleu2)


def ROUGE_L(ss):

  ROUGE = Rouge()

  #合計
  sum_ROUGE_score_f=0
  sum_ROUGE_score_p=0
  sum_ROUGE_score_r=0

  for line in ss:
    index=line[0]
    pred=line[1]

    ROUGE_score=ROUGE.get_scores(index,pred)
    
    sum_ROUGE_score_f+=ROUGE_score[0]['rouge-l']['f']
    sum_ROUGE_score_p+=ROUGE_score[0]['rouge-l']['p']
    sum_ROUGE_score_r+=ROUGE_score[0]['rouge-l']['r']

  #平均
  ROUGE_score_f=sum_ROUGE_score_f/len(ss)
  ROUGE_score_p=sum_ROUGE_score_p/len(ss)
  ROUGE_score_r=sum_ROUGE_score_r/len(ss)

  print("ROUGE_score_F：",ROUGE_score_f)
  print("ROUGE_score_P：",ROUGE_score_p)
  print("ROUGE_score_R：",ROUGE_score_r)


def main():
    ss = read_tsv(sys.argv[1])
    
    Exact_Match(ss)
    Levenstein(ss)
    BLEU1(ss)
    BLEU2(ss)
    ROUGE_L(ss)

main()