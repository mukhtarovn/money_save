
from main.models import FinancialStatement
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in FinancialStatement.objects.all():
            user_fin_state = FinancialStatement.objects.filter(user__username=str(i))
            monthly_expenses = FinancialStatement.objects.get(user__username=str(i))
            user_fin_state.update(expenses_live=monthly_expenses.monthly_expenses)
            print('expenses_live was updated')