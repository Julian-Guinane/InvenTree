from plugins.action.action import ActionPlugin

class AutoSellStock(ActionPlugin):
    """
    An custom plugin to sell out stock to the StockConsumer
    """

    PLUGIN_NAME = "AutoSellStock"
    ACTION_NAME = "autosellstock"

    def perform_action(self):
        print("Action plugin in action!")

    def get_info(self):
        return {
            "user": self.user.username,
            "hello": "world",
        }

    def get_result(self):
        return True

       


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
