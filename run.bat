pytest -s -v -m "sanity" --html=C:\Users\keert\PycharmProjects\Pavan_HybridFramework_SeleniumwithPython\Reports\report.html Testcases/ --browser chrome
rem pytest -s -v -m "sanity or regression" --html=./Reports/report.html Testcases/  --browser chrome
rem pytest -s -v -m "sanity and regression" --html=./Reports/report.html Testcases/  --browser chrome
rem pytest -s -v -m "regression" --html=./Reports/report.html Testcases/  --browser chrome