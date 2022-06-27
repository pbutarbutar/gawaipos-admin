from tabnanny import verbose
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from setting_uom.models import Uom, GroupUom
from merchants.models import Merchant

class Warehouse(models.Model):

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='wh_merchant_id')
    warehouse_name = models.CharField(max_length=50, unique=True)
    warehouse_address = models.CharField(max_length=50)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='wh_merchant_id')
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_wh')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_wh')

    def __str__(self):
        return self.warehouse_name

    class Meta:
        db_table = "warehouses"
        verbose_name_plural = "Warehouses"

class Category(models.Model):
    PART = 'Part'
    SERVICE = 'Service'
    CONSUMABLE = 'Consumable'
    OLI = 'Oli'
    FOOD = 'Food'
    ANOTHER = 'Another'

    ITEMTYPE = (
        (PART, 'Part'),
        (SERVICE, 'Service'),
        (CONSUMABLE, 'Consumable'),
        (OLI, 'OLI'),
        (FOOD, 'FOOD'),
        (ANOTHER, 'Another'),
    )

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='category_merchant_id')
    catogory_tipe = models.CharField(max_length=50, choices=ITEMTYPE, default=PART)
    category_name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_ctg')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_ctg')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'

class ItemOtoClassification(models.Model):

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='item_auto_classification_merchant_id')
    merk = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    pettern = models.CharField(max_length=150)
    ring = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    remarks = models.CharField(max_length=250)

    def __str__(self):
        return self.warehouse_name

class ItemPharmacyClassification(models.Model):

    OBAT_BEBAS = 'Obat Bebas'
    OBAT_KERAS = 'Obat Keras'
    OBAT_TERBATAS = 'Obat Terbatas'
    OBAT_OWA = 'Obat Wajib Apotek (OWA)'
    OBAT_NARKOTIKA = 'Obat Golongan Narkotika'
    OBAT_PSIKOTROPIKA = 'Obat Psikotropika'
    OBAT_HERBAL = 'Obat Herbal'

    GOLONGAN = (
        (OBAT_BEBAS, 'OBAT BEBAS'),
        (OBAT_KERAS, 'Obat Keras'),
        (OBAT_TERBATAS, 'Consumable'),
        (OBAT_OWA, 'Obat Wajib Apotek (OWA)'),
        (OBAT_NARKOTIKA, 'Obat Golongan Narkotika'),
        (OBAT_PSIKOTROPIKA, 'Obat Psikotropika'),
        (OBAT_HERBAL, 'Obat Herbal'),
    )


    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='item_pharmacy_classification_merchant_id')
    kemasan = models.CharField(max_length=50, default="")
    jenis = models.CharField(max_length=150, default="")
    golongan = models.CharField(max_length=50, choices=GOLONGAN, default=OBAT_BEBAS)
    komposisi = models.CharField(max_length=100, default="")
    produsen = models.CharField(max_length=50, default="")
    remarks = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.warehouse_name

class ItemGeneralClassification(models.Model):

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='item_general_classification_merchant_id')
    merk = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    pettern = models.CharField(max_length=150)
    kemasan = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    remarks = models.CharField(max_length=250)

    def __str__(self):
        return self.warehouse_name


class Catalog(models.Model):

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='catalog_merchant_id')
    item_code = models.CharField(max_length=50, unique=True)
    barcode = models.CharField(max_length=50)
    item_name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    uom_group = models.ForeignKey(GroupUom, on_delete=models.CASCADE, null=True, related_name='uom_group_catalog_id')
    uom_inventory = models.ForeignKey(Uom, on_delete=models.CASCADE, null=True , related_name='uom_inventory')
    uom_sales = models.ForeignKey(Uom, on_delete=models.CASCADE, null=True, related_name='uom_sales')
    uom_purchase = models.ForeignKey(Uom, on_delete=models.CASCADE, null=True, related_name='uom_purchase')
    uom_sell_price = models.ForeignKey(Uom, on_delete=models.CASCADE, null=True, related_name='uom_sell_price')
    sell_price = models.IntegerField() 
    sell_disc = models.IntegerField()
    uom_purchase_price = models.ForeignKey(Uom, on_delete=models.CASCADE, null=True, related_name='uom_purchase_price') 
    purchase_price = models.IntegerField()
    purchase_disc = models.IntegerField()
    is_stock = models.BooleanField(default=True)
    stock_minimal = models.IntegerField(default=0) 
    stock_maximal = models.IntegerField(default=0) 
    stock_kritis = models.IntegerField(default=0) 
    general_classification = models.OneToOneField(
        ItemGeneralClassification, 
        null=True,
        on_delete=models.CASCADE
    )
    oto_classification = models.OneToOneField(
        ItemOtoClassification, 
        null=True,
        on_delete=models.CASCADE
    )
    pharmacy_classification = models.OneToOneField(
        ItemPharmacyClassification, 
        null=True,
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_ctlg')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_ctlg')

    def __str__(self):
        return self.item_name

    class Meta:
        db_table = "master_item"
        verbose_name_plural = "Master Item"


class Supplier(models.Model):

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='supplier_merchant_id')
    supplier_code = models.CharField(max_length=50, unique=True)
    supplier_name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.supplier_name

    class Meta:
        db_table = "suppliers"
        verbose_name_plural = "Suppliers"

class Customer(models.Model):
    CASH = 'Cash'
    CREDIT = 'Credit'

    CUSTTYPE = (
        (CASH, 'Cash'),
        (CREDIT, 'Credit'),
    )

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name='customer_merchant_id')
    customer_tipe = models.CharField(max_length=50, choices=CUSTTYPE, default=CASH)
    customer_code = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='create_customer')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='update_customer')

    def __str__(self):
        return self.customer_name

    class Meta:
        db_table = "customers"
        verbose_name_plural = "Customers"

