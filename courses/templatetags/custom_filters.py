from django import template

register = template.Library()

@register.filter
def discounted_price(price, discount):
    try:
        discount_amount = (price * discount) / 100
        return price - discount_amount
    except (ValueError, TypeError):
        return price