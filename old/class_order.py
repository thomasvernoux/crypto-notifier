"""
Author : Thomas Vernoux
Date : 2024-04-07
Description  : This file contain class to manage orders.
"""


class OrderResponse:
    def __init__(self, order):
        self.success                                                   = order['success']
        self.failure_reason                                            = order['failure_reason']
        self.order_id                                                  = order['order_id']
        self.success_response_order_id                                 = order['success_response']['order_id']
        self.succes_response_product_id                                = order['success_response']['product_id']
        self.success_response_side                                     = order['success_response']['side']
        self.success_response_client_order_id                          = order['success_response']['client_order_id']
        self.success_response_order_configuration_market_ioc_base_size = order['order_configuration']['market_market_ioc']['base_size']

class OrderHistory:
    def __init__(self, order:dict):
        """
        Manage an order from client.list_orders()
        """
        self.order_id = order.get('order_id')
        self.product_id = order.get('product_id')
        self.index_usdc = order.get('INDEX-USDC')
        self.user_id = order.get('user_id')
        self.order_configuration_market_ioc_quote_size = order.get('order_configuration', {}).get('market_market_ioc', {}).get('quote_size')
        self.side = order.get('side')
        self.client_order_id = order.get('client_order_id')
        self.client_status = order.get('status')
        self.time_in_force = order.get('time_in_force')
        self.created_time = order.get('created_time')
        self.completion_percentage = order.get('completion_percentage')
        self.filled_size = order.get('filled_size')
        self.average_filled_price = order.get('average_filled_price')
        self.fee = order.get('fee')
        self.number_of_fills = order.get('number_of_fills')
        self.filled_value = order.get('filled_value')
        self.pending_cancel = order.get('pending_cancel')
        self.size_in_quote = order.get('size_in_quote')
        self.total_fees = order.get('total_fees')
        self.size_inclusive_of_fees = order.get('size_inclusive_of_fees')
        self.total_value_after_fees = order.get('total_value_after_fees')
        self.trigger_status = order.get('trigger_status')
        self.order_type = order.get('order_type')
        self.rejected_reason = order.get('reject_reason')
        self.settled = order.get('settled')
        self.product_type = order.get('product_type')
        self.reject_message = order.get('reject_message')
        self.cancel_message = order.get('cancel_message')
        self.order_placement_source = order.get('order_placement_source')
        self.outstanding_hold_amount = order.get('outstanding_hold_amount')
        self.is_liquidation = order.get('is_liquidation')
        self.last_fill_time = order.get('last_fill_time')
        self.edit_history = order.get('edit_history')
        self.leverage = order.get('leverage')
        self.margin_type = order.get('margin_type')
        self.retail_portfolio_id = order.get('retail_portfolio_id')

    def get_str_printable(self):
        ret = ""
        for i in self.__dict__:
            ret += str(i)
            ret += " : "
            ret += str(self.__dict__[i])

        return ret




