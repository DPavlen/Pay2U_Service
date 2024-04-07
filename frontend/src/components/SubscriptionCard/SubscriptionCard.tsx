import { ISubscription } from '../../utils/interfaces/interfaces';
import { styled } from 'styled-components';

interface IUserCardProps {
  card: ISubscription;
}

const Card = styled.div`
  padding: 16px;
  display: flex;
  align-items: center;
  gap: 16px;
  border-radius: 12px;
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.05);
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

  // const price = () => {
  //   if (props.card.tariff.tariff_promo_price || props.card.tariff.tariff_promo_price !== 0) {
  //     if (props.card.tariff.services_duration === '1') {
  //       return props.card.tariff.tariff_promo_price
  //     } else {
  //       return Math.trunc(props.card.tariff.tariff_promo_price / Number(props.card.tariff.services_duration))
  //     }
  //   } else {
  //     return Math.trunc(props.card.tariff.tariff_full_price / Number(props.card.tariff.services_duration))
  //   }
  // }
//TODO Ждем данные об оплате в подписке
  return (
    <Card>
      <CardImg src={props.card.tariff.services.icon_small} alt={props.card.tariff.services.name} />
      <DescriptionWrapper>
        <TitleWrapper>
          <Title>{props.card.tariff.services.name}</Title>
          <span>{props.card.tariff.tariff_full_price} ₽</span>
        </TitleWrapper>
        <NextPayment>
          {'Следующая оплата'}
        </NextPayment>
      </DescriptionWrapper>
    </Card>
  );
}
