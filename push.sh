source venv/bin/activate
pip freeze > requirements.txt
git add .
git commit -m 'update'
git push --repo https://zhenqiangsu:Su650302@github.com/zhenqiangsu/carwasher.git
