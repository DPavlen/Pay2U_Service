import { Link } from 'react-router-dom';
import { IPayment, ISubscription } from '../../utils/interfaces/interfaces';
import { styled } from 'styled-components';

interface IUserCardProps {
  card: IPayment;
}

const Card = styled.div`
  padding: 16px;
  display: flex;
  align-items: center;
  gap: 16px;
  border-radius: 12px;
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.05);
  text-decoration: none;
  color: var(--black);
`;

const CardImg = styled.img`
  max-height: 40px;
`;

const TitleWrapper = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const Title = styled.h3`
  margin: 0;
  font-size: 16px;
  font-weight: 500;
`;

const NextPayment = styled.p`
  margin: 0;
  font-size: 14px;
  font-weight: 600;
  color: var(--grey-2);
`;

const DescriptionWrapper = styled.div`
  display: flex;
  justify-content: flex-start;
  flex-direction: column;
  width: 100%;
  text-align: left;
`;

export default function UserCard(props: IUserCardProps) {

  function formatDate(date: string) {
    const parts = date.split('-');
    return `${parts[2]}.${parts[1]}.${parts[0]}`;
  }
  const parts = props.card.expired_date.split('-');
  const newDate = `${parts[2]}.${parts[1]}.${parts[0]}`;
  const formatedPrice = new Intl.NumberFormat('ru-RU').format(
    props.card.subscription.tariff.tariff_full_price
  );
  return (
    <Card>
      <CardImg
        src={props.card.subscription.tariff.services.icon_small}
        alt={props.card.subscription.tariff.services.name}
      />
      <DescriptionWrapper>
        <TitleWrapper>
          <Title>{props.card.subscription.tariff.services.name}</Title>
          <span>{formatedPrice} ₽</span>
        </TitleWrapper>
        <NextPayment>
          <span>
            {props.card.subscription.auto_payment
              ? `Спишется ${formatDate(props.card.expired_date)}`
              : `Списано ${formatDate(props.card.date)}`}
          </span>
        </NextPayment>
      </DescriptionWrapper>
    </Card>
  );
}
