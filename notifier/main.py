import http_caller
import interpreter


def main():
    program = "Master Inf".replace(" ", "%23")
    semester = "1u2 WS 2021".replace(" ", "%23")
    url = "www.hof-university.de"
    path = f"/index.php?type=1421771406&id=166&tx_stundenplan_stundenplan[controller]=Ajax&tx_stundenplan_stundenplan" \
           f"[action]=loadAenderungen&tx_stundenplan_stundenplan[studiengang]={program}&tx_stundenplan_stundenplan" \
           f"[semester]={semester}&tx_stundenplan_stundenplan[datum]=TT.MM.JJJJ&1634221580821"

    http = http_caller.HttpCaller(url, path)
    content = http.get_content()
    print(f"Timetable changes found: {interpreter.has_changes(content)}")


if __name__ == "__main__":
    main()
