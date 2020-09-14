# Generated by Django 3.0.6 on 2020-09-14 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200914_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('ALL', 'ALL'), ('ACCESSORIES', 'ACCESSORIES'), ('BELTS', 'BELTS'), ('EYEWEAR', 'EYEWEAR'), ('HATS', 'HATS'), ('CAPS', 'CAPS'), ('BEANIES', 'BEANIES'), ('JEWELRY', 'JEWELRY'), ('BRACELETS', 'BRACELETS'), ('EARRINGS', 'EARRINGS'), ('NECKLACES', 'NECKLACES'), ('RINGS', 'RINGS'), ('BAGS', 'BAGS'), ('BACKPACKS', 'BACKPACKS'), ('BRIEFCASES', 'BRIEFCASES'), ('DUFFLE BAGS', 'DUFFLE BAGS'), ('MESSENGER BAGS', 'MESSENGER BAGS'), ('POUCHES', 'POUCHES'), ('TOTE BAGS', 'TOTE BAGS'), ('TRAVEL BAGS', 'TRAVEL BAGS'), ('CLOTHING', 'CLOTHING'), ('TOP', 'TOP'), ('JACKETS', 'JACKETS'), ('DENIM JACKETS', 'DENIM-JACKETS'), ('LEATHER JACKETS', 'LEATHER-JACKETS'), ('DOWN JACKETS', 'DOWN JACKETS'), ('FUR & SHEARLING', 'FUR & SHEARLING'), ('COATS', 'COATS'), ('PEA COATS', 'PEA COATS'), ('LONG COATS', 'LONG COATS'), ('TRENCH COATS', 'TRENCH COATS'), ('SHIRTS', 'SHIRTS'), ('SWEATERS', 'SWEATERS'), ('CARDIGANS', 'CARDIGANS'), ('CREWNECKS', 'CREWNECKS'), ('HOODIES', 'HOODIES'), ('SWEATSHIRTS', 'SWEATSHIRTS'), ('TURTLENECKS', 'TURTLENECKS'), ('V-NECKS', 'V-NECKS'), ('T-SHIRTS', 'T-SHIRTS'), ('TANK TOPS', 'TANK TOPS'), ('POLOS', 'POLOS'), ('BOTTOM', 'BOTTOM'), ('JEANS', 'JEANS'), ('SHORTS', 'SHORTS'), ('PANTS', 'PANTS'), ('CARGO PANTS', 'CARGO PANTS'), ('LEATHER PANTS', 'LEATHER_PANTS'), ('SWEATPANTS', 'SWEATPANTS'), ('TROUSERS', 'TROUSERS'), ('SHOES', 'SHOES'), ('SNEAKERS', 'SNEAKERS'), ('BOOTS', 'BOOTS'), ('LACE UPS', 'LACE UPS'), ('LOAFERS', 'LOAFERS'), ('SANDALS', 'SANDALS')], max_length=100),
        ),
    ]
