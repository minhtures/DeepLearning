# DeepLearning: Phân loại chủ đề cho văn bản báo chi
## Project môn: Học sâu và ứng dụng
Thực hiện bởi nhóm 7:
- Lê Minh Tú
- Nguyễn Đức Tú
- Phạm Quốc Việt
- Nguyễn Tiến Mạnh

## Đề tài: Phân loại chủ đề cho văn bản báo chí
- Dữ liệu tự thu thập từ các trang báo điện tử với hơn 24 nghìn bài báo thuộc 12 chủ đề (số lượng mỗi chủ để tương đương nhau)
- Sử dụng 3 phương pháp khác nhau để mã hóa và huấn luyện
  + TFIDF
  + Word2Vec
  + PhoBERT

## Các thư viện cần sử dụng:
- các mô hình được huấn luyện với tensorflow
-  Xử lý dữ liệu và đánh giá kết quả bằng sklearn
- VNCoreNLP: để tách từ
- transform: để sử dụng pre-trained model PhoBERT
- mô hình W2Vec pretrain: https://github.com/sonvx/word2vecVN

Link data: https://drive.google.com/drive/folders/1l7N6-EK5dYftv2rD9frMlXtVsAevSsiY?usp=sharing
