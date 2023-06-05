from rest_framework import serializers

from sales_chain.models import ChainLink, Contact, Product


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
        ]


class SecondSupplierSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    @staticmethod
    def get_type(obj: ChainLink) -> str:
        """Display unit type from choices"""
        return obj.get_type_display()

    class Meta:
        model = ChainLink
        fields = ['id', 'title', 'type']


class SupplierSerializer(SecondSupplierSerializer):
    supplier = SecondSupplierSerializer()

    class Meta:
        model = ChainLink
        fields = ['id', 'title', 'type', 'supplier']


class ChainLinkSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)
    type = serializers.SerializerMethodField()
    contact = ContactSerializer()
    products = ProductSerializer(many=True)

    def get_type(self, obj):
        return obj.get_type_display()

    class Meta:
        model = ChainLink
        fields = '__all__'


class ChainLinkCreateSerializer(serializers.ModelSerializer):
    supplier = serializers.PrimaryKeyRelatedField(queryset=ChainLink.objects.all())

    class Meta:
        model = ChainLink
        fields = ['title', 'type', 'debt', 'supplier', 'contact', 'products']
        read_only_fields: list[str] = ['debt']
