# Доделать не решённую задачу с семинара:
#
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн,
# вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег


class BankMachine:
    
    MULT = 50
    PERCENT = 0.015
    EXTRA_PERCENT = 0.03
    RICH_PERCENT = 0.10
    COUNT: int
    MAX_SCORE = 5_000_000
    COUNT_LIST: list[str]
    TOTAL_SCORE = 0

    def __init__(self):
        self.COUNT = 0
        self.COUNT_LIST = dict()

    def add_cash(self, cash: int, perc: int) -> tuple[int, int] | None:
        if cash % self.MULT == 0:
            self.TOTAL_SCORE += cash + perc
            self.COUNT += 1
            self.COUNT_LIST[f'+ {cash + perc}'] = 'Успешно'
            return self.TOTAL_SCORE, self.COUNT
        else:
            return None

    def give_cash(self, cash: int, taxes: int, perc: int) -> tuple[int, int] | None:
        if cash % self.MULT == 0 and self.TOTAL_SCORE > 0 and self.TOTAL_SCORE - (cash + taxes + perc) >= 0:
            self.TOTAL_SCORE -= cash + taxes + perc
            self.COUNT += 1
            self.COUNT_LIST[f'- {cash + taxes + perc}'] = 'Успешно'
            return self.TOTAL_SCORE, self.COUNT
        else:
            return None

    def payment_processing(self, cash: int) -> int:
        tmp_cash = cash * self.PERCENT
        min_cash = 30
        max_cash = 600
        if tmp_cash > max_cash:
            tmp_cash = max_cash
        elif tmp_cash < min_cash:
            tmp_cash = min_cash
        else:
            tmp_cash = int(tmp_cash)
        return tmp_cash

    def payment_per(self, cash: int) -> int:
        if cash >=self.MAX_SCORE:
            print(f'\nНачислен налог на богатство! {cash * self.RICH_PERCENT}')
            return cash * self.RICH_PERCENT
        else:
            return 0

    def quit_bank(self):
        return "Всего доброго"

    def add_bonus(self):
            self.TOTAL_SCORE += self.TOTAL_SCORE * self.EXTRA_PERCENT
            return f'Было произведено 3 операции начислено 3%: {int(self.TOTAL_SCORE * self.EXTRA_PERCENT)}\n'

    def count_list(self) -> None:
        for index, op in self.COUNT_LIST.items():
            print(f'{index} - {op}')

    def payment(self, mode: str, cash: int = 0) -> str:
        if self.COUNT % 3 == 0:
             print(self.add_bonus())
        tax = self.payment_per(cash)
        match mode:
            case "add":
                self.add_cash(cash=cash, perc=tax)
                return f"Зачислено успешно! Сумма: {cash}. Баланс: {int(self.TOTAL_SCORE)}"
            case "give":
                commission = self.payment_processing(cash=cash)
                data = self.give_cash(cash=cash, taxes=commission, perc=tax)
                if data:
                    return f"Выдано успешно! Сумма: {cash}. Коммисия: {commission}, " \
                           f"Баланс: {int(self.TOTAL_SCORE)}"
                else:
                    return "Нехватает средств"

            case "list":
                self.count_list()

            case "exit":
                return self.quit_bank()


confirm = BankMachine()
print(confirm.payment(mode='add', cash=2_000_000))
print(confirm.payment(mode='add', cash=1_000_000))
print(confirm.payment(mode='add', cash=1_000_000))
print(confirm.payment(mode='add', cash=3_000_000))
print(confirm.payment(mode='give', cash=5_000_000))
print(confirm.payment(mode='give', cash=2_000_000))
print(confirm.payment(mode='add', cash=230_000))
print(confirm.payment(mode='give', cash=5000000))
print(confirm.payment(mode='list'))