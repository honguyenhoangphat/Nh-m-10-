from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
#client.drop_database('Scraping')
db = client['Scraping']  # chon csdl
collection = db['Oxford_Uni']

def convert_numeric_fields(collection):
    for document in collection.find():
        update_needed = False
        update_fields = {}

        for field, value in document.items():
            # Kiểm tra nếu giá trị là chuỗi và có thể chuyển đổi thành số
            if isinstance(value, str) and value.isdigit():
                update_fields[field] = int(value)  # Chuyển sang kiểu số nguyên
                update_needed = True
            elif isinstance(value, str):
                try:
                    # Cố gắng chuyển thành số thực nếu có thể
                    num_value = float(value)
                    update_fields[field] = num_value
                    update_needed = True
                except ValueError:
                    continue  # Không phải kiểu số, bỏ qua

        # Nếu có bất kỳ trường nào cần cập nhật, thực hiện cập nhật
        if update_needed:
            collection.update_one({'_id': document['_id']}, {'$set': update_fields})
print("Chuyển đổi thành công")