from csv import DictReader

class TransactionAnalyzer():

    def __init__(self):
        
        fr=open("bankanalyzer\\bank_transactions_500_records.csv")

        self.transactions=list(DictReader(fr))

        print(len(self.transactions))

    def debit_transaction(self):

        count=0

        for t in self.transactions:

            if t.get("type")=="debit":

                count+=1

                print(t) 

        print(count)  

    def credit_transaction(self):

        c_coun=0

        for c in self.transactions:

            if c.get("type")=="credit":

                c_coun+=1

                print(c)

                self.k=[c]
        print(self.k,"wehhiwibchweb")
        print(c_coun)        

    def high_value_transactions(self):

        print(max(self.transactions,key=lambda n:n.get("amount")))

    def high_debit_transaction(self):

        for t in self.transactions:

            if t.get("type")=="debit":

                self.maximum=max(self.transactions,key=lambda k:k.get("amount"))

        print("maximum credit value",self.maximum)    

    def high_credit_transaction(self):pass       

Totall_instance=TransactionAnalyzer()
Totall_instance.debit_transaction()
Totall_instance.high_value_transactions()
Totall_instance.credit_transaction()
Totall_instance.high_debit_transaction()