#interfejs strukturalny Notifier - użycie dowolnego kanału (sms,email,slack....)
from typing import Protocol,runtime_checkable,List

@runtime_checkable
class Notifier(Protocol):
    def send(self,to: str, subject: str, body: str) -> None: ...

class EmailNotifier:
    def send(self,to: str, subject: str, body: str) -> None:
        print(f"Email to {to}: {subject}\n{body}")

class SmsNotifier:
    def send(self,to: str, subject: str, body: str) -> None:
        print(f"SMS to {to}: {subject}\n{body}")

def notify_users(users: List[str], notifier: Notifier) -> int:
    sent = 0
    for u in users:
        notifier.send(u,"Hej!",f"Widamość z Protocol Notifier dla Ciebie.")
        sent += 1
    return sent

if __name__ == '__main__':
    count1 = notify_users(["ala@firma.pl","jurek@firma.pl"],EmailNotifier())
    count2 = notify_users(["+48987543235","+12456345789"],SmsNotifier())
    print(count1,count2)
