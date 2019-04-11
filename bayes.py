def Bayes(toplam, negatif, tp, fp):

    positiveresult = total - negative
    negativeprob = negative/total #prior
    testpositive = negativeprob * tp + (positiveresult/total) * fp #predictor

    return negativeprob, testpositive

total = float(input("toplam eleman sayısı: "))
negative = float(input("negatif sayisi : "))
tp = float(input("pozitifken pozitif cıkma: ")) #likelihood, hasta cocugun pozitif olması
fp = float(input("negatifken pozitif cıkma : ")) #Saglıklı cocugun pozitif olması

negativeprob, testpositive = Bayes(total, negative, tp, fp)
print("likelihood = {}, prior = {}, predictor = {}".format(tp, negativeprob, testpositive))
result = (tp * negativeprob) / testpositive
print("sonuc = {}".format(result))
