from module.company import Company


if __name__ == "__main__":
    company = Company('soldiers.csv', 'missions.csv')
    company.assign_tasks()

