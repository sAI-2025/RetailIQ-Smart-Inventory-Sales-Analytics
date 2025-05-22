from django.http import HttpResponse
import random
import string
from datetime import datetime
from .models import OrderDetails
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from .machine_state import Product_live_stock_info


def add_randomvalues(request):
    orders_to_create = []  # List to store orders for bulk creation

    # Generate and save 1,000 random orders
    for _ in range(237):
        ordered_vanilla = random.randint(0, 5)
        ordered_chocolate = random.randint(0, 5)
        ordered_strawberry = random.randint(0, 5)

        # Ensure delivered <= ordered
        delivered_vanilla = random.randint(0, ordered_vanilla)
        delivered_chocolate = random.randint(0, ordered_chocolate)
        delivered_strawberry = random.randint(0, ordered_strawberry)

        # Generate random order
        order = OrderDetails(
            order_id=''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
            payment_id=''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
            device_id=random.randint(1,5),
            ordered_vanilla=ordered_vanilla,
            ordered_chocolate=ordered_chocolate,
            ordered_strawberry=ordered_strawberry,
            delivered_vanilla=delivered_vanilla,
            delivered_chocolate=delivered_chocolate,
            delivered_strawberry=delivered_strawberry,
            is_payment_successful=random.choice([True, False]),
            our_order_id=random.randint(0, 999999),
            is_all_items_delivered=random.choice([True, False])
        )
        orders_to_create.append(order)

    # Bulk create for better performance
    OrderDetails.objects.bulk_create(orders_to_create)

    # Count total rows after insertion
    total_count = OrderDetails.objects.count()

    return HttpResponse(f"Inserted 1000 random order entries. Total rows in table: {total_count}")


def total_rows(request):
    # Get the total number of rows in the table
    total_count = OrderDetails.objects.count()

    # HTML content with inline total count
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Total Rows</title>
    </head>
    <body>
        <h1>Total Rows in OrderDetails Table</h1>
        <p>The total number of rows in the OrderDetails table is: {total_count}</p>
    </body>
    </html>
    """

    # Return an HttpResponse with the HTML content
    return HttpResponse(html_content)
def live_values(request):
    """Render the live product stock values as an HTML table directly from view."""

    html = """
    <html>
    <head>
        <title>Live Product Stock</title>
        <style>
            table {
                width: 60%;
                border-collapse: collapse;
                margin: 40px auto;
            }
            th, td {
                border: 1px solid #888;
                padding: 10px;
                text-align: center;
            }
            th {
                background-color: #f2f2f2;
            }
            caption {
                margin-bottom: 15px;
                font-size: 20px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <table>
            <caption>Live Product Stock</caption>
            <thead>
                <tr>
                    <th>Product ID</th>
                    <th>Vanilla</th>
                    <th>Chocolate</th>
                    <th>Strawberry</th>
                </tr>
            </thead>
            <tbody>
    """

    for product_id, flavors in Product_live_stock_info.items():
        vanilla = flavors.get('vanilla', 0)
        chocolate = flavors.get('chocolate', 0)
        strawberry = flavors.get('strawberry', 0)

        html += f"""
            <tr>
                <td>{product_id}</td>
                <td>{vanilla}</td>
                <td>{chocolate}</td>
                <td>{strawberry}</td>
            </tr>
        """

    html += """
            </tbody>
        </table>
    </body>
    </html>
    """

    return HttpResponse(html)

