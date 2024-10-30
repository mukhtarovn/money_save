from django.contrib import admin

# Register your models here.
from main.models import Income, NecessaryExpenses, Category, CategoryIncomes, \
 FinancialStatement


# admin.site.register(Income)



@admin.register(Income)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'category','sum','description', 'time_create']
    ordering = ('user',)
    search_fields = ['user', 'time_create']
    # list_filter = (
    #     # ('user', admin.EmptyFieldListFilter),
    #     ('category', admin.EmptyFieldListFilter),
    #     ('time_create', admin.EmptyFieldListFilter),
    # )
@admin.register(NecessaryExpenses)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'category','sum','description', 'time_create', 'time_update']
    ordering = ('user',)
    search_fields = ['user', 'category']
    # list_filter = (
    #     # ('user', admin.EmptyFieldListFilter),
    #     ('category', admin.EmptyFieldListFilter),
    #     ('time_create', admin.EmptyFieldListFilter),
    # )

# @admin.register(DailyExpenses)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id','user','category','sum', 'description', 'time_create']
#     ordering = ('user',)
#     search_fields = ['user', 'category', 'sum']\

# @admin.register(DailyIncoms)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id','user','category','sum', 'description', 'time_create']
#     ordering = ('user',)
#     search_fields = ['user', 'category', 'sum']

@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'user']
    ordering = ('name',)

@admin.register(CategoryIncomes)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'user']
    ordering = ('name',)

@admin.register(FinancialStatement)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'monthly_incoms', 'monthly_expenses', 'monthly_target', 'expenses_live']
    ordering = ('user',)