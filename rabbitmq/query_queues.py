import requests

# API 接口的 URL
url = 'http://xxxx/api/queues'

# 替换为你的 RabbitMQ 用户名和密码
username = 'xxx'
password = 'xxx'

try:
    # 发送带有认证信息的 GET 请求
    response = requests.get(url, auth=(username, password))

    # 检查响应状态码
    if response.status_code == 200:
        # 获取 JSON 数据
        queues_data = response.json()

        # 筛选出 messages_ready 大于 0 的队列名称
        queues_with_messages = []
        for queue in queues_data:
            if queue.get('messages_ready', 0) > 0:
                queues_with_messages.append(queue['name'])

        # 输出结果
        if queues_with_messages:
            print("messages_ready 大于 0 的队列名称:")
            for queue_name in queues_with_messages:
                print(queue_name)
        else:
            print("没有 messages_ready 大于 0 的队列。")
    else:
        print(f"请求失败，状态码: {response.status_code}")

except requests.RequestException as e:
    print(f"请求发生错误: {e}")