import speedtest
import ssl 

def run_speed_test():
    print("Connecting to the best available server... Please wait!")

    ssl._create_default_https_context = ssl._create_unverified_context

    st = speedtest.Speedtest(secure=True)

    st.get_best_server()

    print("Testing download speed...")
    download_speed = st.download()

    print("Testing upload speed...")
    upload_speed = st.upload()

    ping = st.results.ping 

    downlaod_mbps = download_speed / 1024 / 1024
    float_download = f"{downlaod_mbps:.2f}"

    upload_mbps = upload_speed / 1024 / 1024
    float_upload = f"{upload_mbps:.2f}"

    


    print("\n=== SPEED TEST RESULTS ===")
    print(f"Download Speed: {float_download} Mbps") 
    print(f"Upload Speed: {float_upload} Mbps") 
    print(f"Ping: {ping} ms") 
    print("==========================") 

if __name__ == "__main__": 
    run_speed_test()
