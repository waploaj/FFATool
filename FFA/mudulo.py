# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EmployeePerson(models.Model):

    class Meta:
        managed = False
        db_table = 'Employee_person'


class PersonPerson(models.Model):
    person_id = models.CharField(primary_key=True, max_length=50)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Person_person'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OsposAppConfig(models.Model):
    key = models.CharField(primary_key=True, max_length=50)
    value = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'ospos_app_config'


class OsposCustomers(models.Model):
    person = models.ForeignKey('OsposPeople', models.DO_NOTHING)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    taxable = models.IntegerField()
    sales_tax_code = models.CharField(max_length=32)
    discount_percent = models.DecimalField(max_digits=15, decimal_places=2)
    package = models.ForeignKey('OsposCustomersPackages', models.DO_NOTHING, blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_customers'


class OsposCustomersPackages(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=255, blank=True, null=True)
    points_percent = models.FloatField()
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_customers_packages'


class OsposCustomersPoints(models.Model):
    person = models.ForeignKey(OsposCustomers, models.DO_NOTHING)
    package = models.ForeignKey(OsposCustomersPackages, models.DO_NOTHING)
    sale = models.ForeignKey('OsposSales', models.DO_NOTHING)
    points_earned = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_customers_points'


class OsposDinnerTables(models.Model):
    dinner_table_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    status = models.IntegerField()
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_dinner_tables'


class OsposEmployees(models.Model):
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    person = models.ForeignKey('OsposPeople', models.DO_NOTHING)
    deleted = models.IntegerField()
    hash_version = models.IntegerField()
    language = models.CharField(max_length=48, blank=True, null=True)
    language_code = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ospos_employees'


class OsposGiftcards(models.Model):
    record_time = models.DateTimeField()
    giftcard_id = models.AutoField(primary_key=True)
    giftcard_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    deleted = models.IntegerField()
    person = models.ForeignKey('OsposPeople', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ospos_giftcards'


class OsposGrants(models.Model):
    permission = models.OneToOneField('OsposPermissions', models.DO_NOTHING, primary_key=True)
    person = models.ForeignKey(OsposEmployees, models.DO_NOTHING)
    menu_group = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ospos_grants'
        unique_together = (('permission', 'person'),)


class OsposInventory(models.Model):
    trans_id = models.AutoField(primary_key=True)
    trans_items = models.ForeignKey('OsposItems', models.DO_NOTHING, db_column='trans_items')
    trans_user = models.ForeignKey(OsposEmployees, models.DO_NOTHING, db_column='trans_user')
    trans_date = models.DateTimeField()
    trans_comment = models.TextField()
    trans_location = models.ForeignKey('OsposStockLocations', models.DO_NOTHING, db_column='trans_location')
    trans_inventory = models.DecimalField(max_digits=15, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'ospos_inventory'


class OsposItemKitItems(models.Model):
    item_kit = models.OneToOneField('OsposItemKits', models.DO_NOTHING, primary_key=True)
    item = models.ForeignKey('OsposItems', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=15, decimal_places=3)
    kit_sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_item_kit_items'
        unique_together = (('item_kit', 'item', 'quantity'),)


class OsposItemKits(models.Model):
    item_kit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    item_id = models.IntegerField()
    kit_discount_percent = models.DecimalField(max_digits=15, decimal_places=2)
    price_option = models.IntegerField()
    print_option = models.IntegerField()
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ospos_item_kits'


class OsposItemQuantities(models.Model):
    item = models.OneToOneField('OsposItems', models.DO_NOTHING, primary_key=True)
    location = models.ForeignKey('OsposStockLocations', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=15, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'ospos_item_quantities'
        unique_together = (('item', 'location'),)


class OsposItems(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    supplier = models.ForeignKey('OsposSuppliers', models.DO_NOTHING, blank=True, null=True)
    item_number = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255)
    cost_price = models.DecimalField(max_digits=15, decimal_places=2)
    unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    reorder_level = models.DecimalField(max_digits=15, decimal_places=3)
    receiving_quantity = models.DecimalField(max_digits=15, decimal_places=3)
    item_id = models.AutoField(primary_key=True)
    pic_filename = models.CharField(max_length=255, blank=True, null=True)
    allow_alt_description = models.IntegerField()
    is_serialized = models.IntegerField()
    stock_type = models.IntegerField()
    item_type = models.IntegerField()
    tax_category_id = models.IntegerField()
    deleted = models.IntegerField()
    custom1 = models.CharField(max_length=255, blank=True, null=True)
    custom2 = models.CharField(max_length=255, blank=True, null=True)
    custom3 = models.CharField(max_length=255, blank=True, null=True)
    custom4 = models.CharField(max_length=255, blank=True, null=True)
    custom5 = models.CharField(max_length=255, blank=True, null=True)
    custom6 = models.CharField(max_length=255, blank=True, null=True)
    custom7 = models.CharField(max_length=255, blank=True, null=True)
    custom8 = models.CharField(max_length=255, blank=True, null=True)
    custom9 = models.CharField(max_length=255, blank=True, null=True)
    custom10 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ospos_items'


class OsposItemsTaxes(models.Model):
    item = models.OneToOneField(OsposItems, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=255)
    percent = models.DecimalField(max_digits=15, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'ospos_items_taxes'
        unique_together = (('item', 'name', 'percent'),)


class OsposMarketinfo(models.Model):
    posm = models.CharField(max_length=255)
    promomaterial = models.CharField(max_length=255)
    ourprouct = models.CharField(max_length=255)
    person = models.ForeignKey(OsposCustomers, models.DO_NOTHING)
    posm_id = models.IntegerField(primary_key=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ospos_marketinfo'


class OsposModules(models.Model):
    name_lang_key = models.CharField(unique=True, max_length=255)
    desc_lang_key = models.CharField(unique=True, max_length=255)
    sort = models.IntegerField()
    module_id = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'ospos_modules'


class OsposPeople(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    comments = models.TextField()
    person_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ospos_people'


class OsposPermissions(models.Model):
    permission_id = models.CharField(primary_key=True, max_length=255)
    module = models.ForeignKey(OsposModules, models.DO_NOTHING)
    location = models.ForeignKey('OsposStockLocations', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ospos_permissions'


class OsposReceivings(models.Model):
    receiving_time = models.DateTimeField()
    supplier = models.ForeignKey('OsposSuppliers', models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(OsposEmployees, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    receiving_id = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=20, blank=True, null=True)
    reference = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ospos_receivings'


class OsposReceivingsItems(models.Model):
    receiving = models.OneToOneField(OsposReceivings, models.DO_NOTHING, primary_key=True)
    item = models.ForeignKey(OsposItems, models.DO_NOTHING)
    description = models.CharField(max_length=30, blank=True, null=True)
    serialnumber = models.CharField(max_length=30, blank=True, null=True)
    line = models.IntegerField()
    quantity_purchased = models.DecimalField(max_digits=15, decimal_places=3)
    item_cost_price = models.DecimalField(max_digits=15, decimal_places=2)
    item_unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=15, decimal_places=2)
    item_location = models.IntegerField()
    receiving_quantity = models.DecimalField(max_digits=15, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'ospos_receivings_items'
        unique_together = (('receiving', 'item', 'line'),)


class OsposSales(models.Model):
    sale_time = models.DateTimeField()
    customer = models.ForeignKey(OsposCustomers, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(OsposEmployees, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    invoice_number = models.CharField(unique=True, max_length=32, blank=True, null=True)
    quote_number = models.CharField(max_length=32, blank=True, null=True)
    sale_id = models.AutoField(primary_key=True)
    sale_status = models.IntegerField()
    dinner_table = models.ForeignKey(OsposDinnerTables, models.DO_NOTHING, blank=True, null=True)
    work_order_number = models.CharField(max_length=32, blank=True, null=True)
    sale_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_sales'


class OsposSalesItems(models.Model):
    sale = models.OneToOneField(OsposSales, models.DO_NOTHING, primary_key=True)
    item = models.ForeignKey(OsposItems, models.DO_NOTHING)
    description = models.CharField(max_length=255, blank=True, null=True)
    serialnumber = models.CharField(max_length=30, blank=True, null=True)
    line = models.IntegerField()
    quantity_purchased = models.DecimalField(max_digits=15, decimal_places=3)
    item_cost_price = models.DecimalField(max_digits=15, decimal_places=2)
    item_unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=15, decimal_places=2)
    item_location = models.ForeignKey('OsposStockLocations', models.DO_NOTHING, db_column='item_location')
    print_option = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_sales_items'
        unique_together = (('sale', 'item', 'line'),)


class OsposSalesItemsTaxes(models.Model):
    sale = models.OneToOneField(OsposSalesItems, models.DO_NOTHING, primary_key=True)
    item = models.ForeignKey(OsposItems, models.DO_NOTHING)
    line = models.IntegerField()
    name = models.CharField(max_length=255)
    percent = models.DecimalField(max_digits=15, decimal_places=4)
    tax_type = models.IntegerField()
    rounding_code = models.IntegerField()
    cascade_tax = models.IntegerField()
    cascade_sequence = models.IntegerField()
    item_tax_amount = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'ospos_sales_items_taxes'
        unique_together = (('sale', 'item', 'line', 'name', 'percent'),)


class OsposSalesPayments(models.Model):
    sale = models.OneToOneField(OsposSales, models.DO_NOTHING, primary_key=True)
    payment_type = models.CharField(max_length=40)
    payment_amount = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ospos_sales_payments'
        unique_together = (('sale', 'payment_type'),)


class OsposSalesRewardPoints(models.Model):
    sale = models.ForeignKey(OsposSales, models.DO_NOTHING)
    earned = models.FloatField()
    used = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ospos_sales_reward_points'


class OsposSalesTaxes(models.Model):
    sale_id = models.IntegerField(primary_key=True)
    tax_type = models.SmallIntegerField()
    tax_group = models.CharField(max_length=32)
    sale_tax_basis = models.DecimalField(max_digits=15, decimal_places=4)
    sale_tax_amount = models.DecimalField(max_digits=15, decimal_places=4)
    print_sequence = models.IntegerField()
    name = models.CharField(max_length=255)
    tax_rate = models.DecimalField(max_digits=15, decimal_places=4)
    sales_tax_code = models.CharField(max_length=32)
    rounding_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_sales_taxes'
        unique_together = (('sale_id', 'tax_type', 'tax_group'),)


class OsposSessions(models.Model):
    id = models.CharField(max_length=40)
    ip_address = models.CharField(max_length=45)
    timestamp = models.PositiveIntegerField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'ospos_sessions'


class OsposStockLocations(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_stock_locations'


class OsposSuppliers(models.Model):
    person = models.ForeignKey(OsposPeople, models.DO_NOTHING)
    company_name = models.CharField(max_length=255)
    agency_name = models.CharField(max_length=255)
    account_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_suppliers'


class OsposTaxCategories(models.Model):
    tax_category_id = models.AutoField(primary_key=True)
    tax_category = models.CharField(max_length=32)
    tax_group_sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_tax_categories'


class OsposTaxCodeRates(models.Model):
    rate_tax_code = models.CharField(primary_key=True, max_length=32)
    rate_tax_category_id = models.IntegerField()
    tax_rate = models.DecimalField(max_digits=15, decimal_places=4)
    rounding_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_tax_code_rates'
        unique_together = (('rate_tax_code', 'rate_tax_category_id'),)


class OsposTaxCodes(models.Model):
    tax_code = models.CharField(primary_key=True, max_length=32)
    tax_code_name = models.CharField(max_length=255)
    tax_code_type = models.IntegerField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ospos_tax_codes'
