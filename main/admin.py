from django.contrib import admin

# Register your models here.
from main.models import Income, NecessaryExpenses, DailyExpenses, Category, DailyIncoms, CategoryIncomes, \
    UserCategoryExpenses, UserCategoryIncomes


# admin.site.register(Income)
# admin.site.register(NecessaryExpenses)
# admin.site.register(Category)


@admin.register(Income)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'description']
    ordering = ('user',)
    # search_fields = ['last_name', 'first_name']
    # list_filter = (
    #     ('user', admin.EmptyFieldListFilter),
    #     ('income', admin.EmptyFieldListFilter),
    # )
@admin.register(NecessaryExpenses)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'category','sum','description', 'time_create', 'time_update']
    ordering = ('user',)
    search_fields = ['user', 'category']
    # list_filter = (
    #     ('user', admin.EmptyFieldListFilter),
    #     ('email', admin.EmptyFieldListFilter),
    # )

@admin.register(DailyExpenses)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','user','category','sum', 'description', 'time_create']
    ordering = ('user',)
    search_fields = ['user', 'category', 'sum']\

@admin.register(DailyIncoms)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','user','category','sum', 'description', 'time_create']
    ordering = ('user',)
    search_fields = ['user', 'category', 'sum']

@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ('name',)

@admin.register(CategoryIncomes)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ('name',)

@admin.register(UserCategoryExpenses)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'description']
    ordering = ('name',)

@admin.register(UserCategoryIncomes)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'description']
    ordering = ('name',)