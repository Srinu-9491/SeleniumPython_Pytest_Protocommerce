import openpyxl


class HomePageData:

    # If we declare any method as static we can call this directly with class reference, no need to create a object of the class
    @staticmethod
    def getTestData(testcase_name):
        Dict = {}
        book = openpyxl.load_workbook("C:\\Users\\kondsrin\\PycharmProjects\\pytestframework_protocommerce\\TestData\\excelDemoPython.xlsx")
        sheet = book.active
        for i in range(1, sheet.max_row + 1):
            if sheet.cell(row=i, column=1).value == testcase_name:
                for j in range(2, sheet.max_column + 1):
                    Dict[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value
        return [Dict]
