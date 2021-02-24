
# blogの作成
## djangoでblogサイトを構築しherokuでデプロイ
- class based view で作成
- TopView,CategoryDetailViewでは複数のmodelを扱えるように実装
- bootstrapで装飾。レスポンシブな見た目にした
- herokuでデプロイ
- 画像アップロードにはcloudinaryを使用
- heroku環境でPostgresを使用するためdj_database_urlを使用
- whitenoiseで静的ファイルを配信
