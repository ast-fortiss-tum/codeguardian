# Source: Row 16 in ./dataset/CVEfixes/Analysis/results/Python/df_python_cwe_863.xlsx

def resolve_orders(root: models.User, info, **kwargs):
        from ..order.types import OrderCountableConnection

        def _resolve_orders(orders):
            requester = get_user_or_app_from_context(info.context)
            if not requester.has_perm(OrderPermissions.MANAGE_ORDERS):
                # allow fetch requestor orders (except drafts)
                if root == info.context.user:
                    orders = list(
                        filter(lambda order: order.status != OrderStatus.DRAFT, orders)
                    )
                else:
                    raise PermissionDenied()

            return create_connection_slice(
                orders, info, kwargs, OrderCountableConnection
            )

        return OrdersByUserLoader(info.context).load(root.id).then(_resolve_orders)