
from sqlalchemy import Column, Integer, String
from database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer)
    email = Column(String)
    password_hash = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    role_id = Column(Integer)
    created_at = Column(String)
    updated_at = Column(String)


class Roles(Base):
    __tablename__ = 'roles'

    id = Column(Integer)
    name = Column(String)
    description = Column(String)


class Permissions(Base):
    __tablename__ = 'permissions'

    id = Column(Integer)
    name = Column(String)
    description = Column(String)


class Role_permissions(Base):
    __tablename__ = 'role_permissions'

    role_id = Column(Integer)
    permission_id = Column(Integer)


class Contacts(Base):
    __tablename__ = 'contacts'

    id = Column(Integer)
    user_id = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)
    company = Column(String)
    title = Column(String)
    notes = Column(String)
    created_at = Column(String)
    updated_at = Column(String)


class Subscription_plans(Base):
    __tablename__ = 'subscription_plans'

    id = Column(Integer)
    name = Column(String)
    description = Column(String)
    price = Column(String)
    currency = Column(String)
    duration_days = Column(Integer)
    is_active = Column(String)
    created_at = Column(String)
    updated_at = Column(String)


class Subscriptions(Base):
    __tablename__ = 'subscriptions'

    id = Column(Integer)
    user_id = Column(Integer)
    plan_id = Column(Integer)
    start_date = Column(String)
    end_date = Column(String)
    status = Column(String)
    auto_renew = Column(String)
    created_at = Column(String)
    updated_at = Column(String)


class Payments(Base):
    __tablename__ = 'payments'

    id = Column(Integer)
    user_id = Column(Integer)
    subscription_id = Column(Integer)
    amount = Column(String)
    currency = Column(String)
    transaction_id = Column(String)
    payment_method = Column(String)
    status = Column(String)
    payment_date = Column(String)
    created_at = Column(String)
    updated_at = Column(String)


class Analytics_data(Base):
    __tablename__ = 'analytics_data'

    id = Column(Integer)
    user_id = Column(Integer)
    event_name = Column(String)
    event_data = Column(String)
    timestamp = Column(String)
    ip_address = Column(String)
    user_agent = Column(String)

