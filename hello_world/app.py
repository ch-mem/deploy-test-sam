import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    Lambda関数のエントリーポイント

    Parameters:
        event: APIGatewayからのイベント情報
        context: Lambda実行環境のコンテキスト情報

    Returns:
        dict: APIGatewayへのレスポンス
    """
    logger.info(f"Received event: {json.dumps(event)}")

    # クエリパラメータから名前を取得（デフォルトは "World"）
    query_params = event.get('queryStringParameters') or {}
    name = query_params.get('name', 'World')

    response_body = {
        'message': f'Hello, {name}!',
        'input': event
    }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(response_body, ensure_ascii=False)
    }
