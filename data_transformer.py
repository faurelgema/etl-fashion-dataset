import pandas as pd

def transform_json_to_dataframe(json_data):
    rows = []
    for data in json_data:
        sku_name = data['item_group_name']
        for sku in data['product_skus']:
            barcode = sku['item_code']
            for variation in sku['variation_values']:
                size = variation['value']
                sell_price_dict = {price['channel_id']: price['sell_price'] for price in sku['prices']}

                channel_map = {
                    4: 'Lazada',
                    8: 'Zalora',
                    32: 'Blibli',
                    64: 'Shopee',
                    128: 'Tokopedia',
                    131076: 'Tiktok',
                    1048576: 'Shopify'
                } 
                rows.append({
                    'Barcode': barcode,
                    'Size': size,
                    'SKU': sku_name,
                    'Lazada': sell_price_dict.get(4, 0),
                    'Zalora': sell_price_dict.get(8, 0),
                    'Blibli': sell_price_dict.get(32, 0),
                    'Shopee': sell_price_dict.get(64, 0),
                    'Tokopedia': sell_price_dict.get(128, 0),
                    'Tiktok': sell_price_dict.get(131076, 0),
                    'Shopify': sell_price_dict.get(1048576, 0)
                })
    return pd.DataFrame(rows)
