def main():

    file_name = input("Write the file name\n").lower().strip()
    match file_name[-4:]:
        case ".gif":
            print("image/gif")
        case ".jpg" | "jpeg":
            print("image/jpeg")
        case ".png":
            print("image/png")
        case ".pdf":
            print("application/pdf")
        case ".txt":
            print("text/plain")
        case ".zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

main()
