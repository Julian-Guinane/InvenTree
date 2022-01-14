from plugins.action.action import ActionPlugin
from company.models import Company
from order.models import SalesOrder
import datetime

class AutoSellStock(ActionPlugin):
    """
    An custom plugin to sell out stock to the StockConsumer
    """

    PLUGIN_NAME = "AutoSellStock"
    ACTION_NAME = "autosellstock"

    def perform_action(self):
        # find stock consumer
        stockconsumer = Company.objects.get(name='StockConsumer')
        print(stockconsumer)
        print(AutoSellStock.get_fresh_so(stockconsumer))
        
        
        # get latest non-stale sell order TODO implement stale days extraction
        # find and add items to sell order
        

    def get_info(self):
        return {
            "user": self.user.username
        }

    def get_result(self):
        return ""

    @staticmethod
    def get_fresh_so(customer, stale_time=1):
        """
        Get most recent sales order within the stale time.
        
        Parameters
        ----------
        customer : Company
            Company to check sales order from
        stale_time : int, optional
            Time in days to consider most recent sales order stale (default is 1)
        Returns
        -------
        fresh_so : SalesOrder
            Most recent sales order within stale time. Returns None if no fresh sales orders.
        """
        freshDate = datetime.date.today() - datetime.timedelta(days = stale_time)
        # status of 10 corresponds to pending orders
        freshOrders = SalesOrder.objects.filter(
                        customer_id=customer.id,
                        creation_date__gte=freshDate,
                        status=10)
        if len(freshOrders):
          freshestOrder = freshOrders.order_by('creation_date')[0]
        else:
            freshestOrder = None  
            
        return freshestOrder
        

       


    # def __init__(self, user, data=None):
    #     """
    #     An action plugin takes a user reference, and an optional dataset (dict)
    #     """
    #     plugin.InvenTreePlugin.__init__(self)

    #     self.user = user
    #     self.data = data

    # def perform_action(self):
    #     """
    #     Override this method to perform the action!
    #     """
    #     pass

    # def get_result(self):
    #     """
    #     Result of the action?
    #     """

    #     # Re-implement this for cutsom actions
    #     return False

    # def get_info(self):
    #     """
    #     Extra info? Can be a string / dict / etc
    #     """
    #     return None

    # def get_response(self):
    #     """
    #     Return a response. Default implementation is a simple response
    #     which can be overridden.
    #     """
    #     return {
    #         "action": self.action_name(),
    #         "result": self.get_result(),
    #         "info": self.get_info(),
    #     }
